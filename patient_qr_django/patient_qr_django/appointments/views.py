from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Appointment
from patients.models import Patient
from doctors.models import Doctor

def appointment_list(request):
    """Display all appointments"""
    appointments = Appointment.objects.all().select_related('patient', 'doctor')
    context = {
        'appointments': appointments
    }
    return render(request, 'appointments/appointment_list.html', context)

def appointment_create(request):
    """Create a new appointment"""
    if request.method == 'POST':
        patient_id = request.POST.get('patient')
        doctor_id = request.POST.get('doctor')
        date = request.POST.get('date')
        reason = request.POST.get('reason')
        
        try:
            patient = Patient.objects.get(id=patient_id)
            doctor = Doctor.objects.get(id=doctor_id)
            
            appointment = Appointment.objects.create(
                patient=patient,
                doctor=doctor,
                date=date,
                reason=reason
            )
            messages.success(request, 'Appointment created successfully!')
            return redirect('appointments:list')
        except Exception as e:
            messages.error(request, f'Error creating appointment: {str(e)}')
    
    patients = Patient.objects.all()
    doctors = Doctor.objects.all()
    context = {
        'patients': patients,
        'doctors': doctors
    }
    return render(request, 'appointments/appointment_create.html', context)

def appointment_cancel(request, pk):
    """Cancel an appointment"""
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment.status = 'cancelled'
    appointment.save()
    messages.success(request, 'Appointment cancelled successfully!')
    return redirect('appointments:list')
