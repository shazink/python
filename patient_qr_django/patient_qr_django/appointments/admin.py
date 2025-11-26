from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor', 'date', 'status', 'created_at']
    search_fields = ['patient__name', 'doctor__name', 'reason']
    list_filter = ['status', 'date', 'doctor']
    autocomplete_fields = ['patient', 'doctor']
