from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment
from django.utils import timezone
import datetime

class Command(BaseCommand):
    help = 'Create admin user and sample data for all modules'

    def handle(self, *args, **kwargs):
        # 1. Create superuser
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write(self.style.SUCCESS('✅ Superuser created! (admin/admin123)'))
        else:
            self.stdout.write('ℹ️ Superuser already exists')

        # 2. Create Doctors
        doctors_data = [
            {'name': 'Dr. Sarah Wilson', 'specialization': 'Cardiologist', 'phone': '+91 9876543300'},
            {'name': 'Dr. John Smith', 'specialization': 'Pediatrician', 'phone': '+91 9876543301'},
            {'name': 'Dr. Emily Chen', 'specialization': 'Dermatologist', 'phone': '+91 9876543302'},
        ]
        
        for data in doctors_data:
            doc, created = Doctor.objects.get_or_create(name=data['name'], defaults=data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'✅ Doctor created: {doc.name}'))

        # 3. Create Patients
        patients_data = [
            {'name': 'Rajesh Kumar', 'age': 45, 'phone': '+91 9876543210', 'blood_group': 'O+', 'disease': 'Hypertension'},
            {'name': 'Priya Sharma', 'age': 32, 'phone': '+91 9876543211', 'blood_group': 'A+', 'disease': 'Type 2 Diabetes'},
            {'name': 'Amit Patel', 'age': 28, 'phone': '+91 9876543212', 'blood_group': 'B+', 'disease': 'Viral Fever'},
        ]

        for data in patients_data:
            pat, created = Patient.objects.get_or_create(name=data['name'], defaults=data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'✅ Patient created: {pat.name}'))
            elif not pat.disease and 'disease' in data:
                pat.disease = data['disease']
                pat.generate_qr_code()
                pat.save()
                self.stdout.write(self.style.SUCCESS(f'🔄 Updated patient: {pat.name}'))

        # 4. Create Appointments
        # Link Rajesh to Dr. Sarah (Cardiologist)
        pat1 = Patient.objects.get(name='Rajesh Kumar')
        doc1 = Doctor.objects.get(name='Dr. Sarah Wilson')
        
        # Link Priya to Dr. Emily (Dermatologist)
        pat2 = Patient.objects.get(name='Priya Sharma')
        doc2 = Doctor.objects.get(name='Dr. Emily Chen')
        
        appointments_data = [
            {
                'patient': pat1, 'doctor': doc1, 
                'date': timezone.now() + datetime.timedelta(days=2),
                'reason': 'Regular checkup for hypertension',
                'status': 'scheduled'
            },
            {
                'patient': pat2, 'doctor': doc2, 
                'date': timezone.now() + datetime.timedelta(days=1),
                'reason': 'Skin rash consultation',
                'status': 'scheduled'
            },
        ]
        
        for data in appointments_data:
            if not Appointment.objects.filter(patient=data['patient'], doctor=data['doctor'], date=data['date']).exists():
                appt = Appointment.objects.create(**data)
                self.stdout.write(self.style.SUCCESS(f'✅ Appointment scheduled: {appt}'))

        self.stdout.write(self.style.SUCCESS('\n🎉 All modules populated successfully!'))
        self.stdout.write('\n📱 Visit http://127.0.0.1:8000/admin/ to see all 3 modules')
