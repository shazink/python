from django.db import models
from django.core.files.base import ContentFile
import qrcode
from io import BytesIO
import random
import string
from doctors.models import Doctor

class Patient(models.Model):
    # Patient information
    patient_id = models.CharField(max_length=10, unique=True, blank=True, editable=False)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=15)
    disease = models.CharField(max_length=200, blank=True, help_text="Main complaint or diagnosis")
    blood_group = models.CharField(max_length=5, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True, related_name='patients')
    
    # QR Code
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.patient_id} - {self.name}"
    
    def generate_patient_id(self):
        """Generate unique patient ID"""
        while True:
            # Generate ID like PAT00001
            random_num = ''.join(random.choices(string.digits, k=5))
            patient_id = f"PAT{random_num}"
            if not Patient.objects.filter(patient_id=patient_id).exists():
                return patient_id
    
    def generate_qr_code(self):
        """Generate QR code for patient"""
        # QR code data
        qr_data = f"""
Patient ID: {self.patient_id}
Name: {self.name}
Age: {self.age}
Phone: {self.phone}
Disease: {self.disease}
Blood Group: {self.blood_group}
Doctor: {self.doctor.name if self.doctor else "Not Assigned"}
        """.strip()
        
        # Create QR code
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save to buffer
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        buffer.seek(0)
        
        # Save to model
        filename = f'qr_{self.patient_id}.png'
        self.qr_code.save(filename, ContentFile(buffer.read()), save=False)
    
    def save(self, *args, **kwargs):
        # Generate patient ID if not exists
        if not self.patient_id:
            self.patient_id = self.generate_patient_id()
        
        # Save first to get ID
        super().save(*args, **kwargs)
        
        # Generate QR code after saving
        if not self.qr_code:
            self.generate_qr_code()
            super().save(update_fields=['qr_code'])
