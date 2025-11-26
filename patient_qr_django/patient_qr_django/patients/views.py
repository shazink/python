from django.shortcuts import render, get_object_or_404
from .models import Patient

def patient_list(request):
    """Display all patients"""
    patients = Patient.objects.all()
    return render(request, 'patients/patient_list.html', {'patients': patients})

def patient_qr(request, patient_id):
    """Display patient QR code"""
    patient = get_object_or_404(Patient, patient_id=patient_id)
    return render(request, 'patients/patient_qr.html', {'patient': patient})
