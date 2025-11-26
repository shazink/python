from django.contrib import admin
from .models import Patient
from django.utils.html import format_html

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['patient_id', 'name', 'age', 'disease', 'phone', 'qr_code_preview', 'created_at']
    search_fields = ['patient_id', 'name', 'phone', 'disease']
    list_filter = ['blood_group', 'created_at']
    readonly_fields = ['patient_id', 'qr_code_display', 'created_at', 'updated_at']
    
    fields = ['name', 'age', 'disease', 'phone', 'blood_group', 'patient_id', 'qr_code_display', 'created_at', 'updated_at']
    
    def qr_code_preview(self, obj):
        """Show small QR code in list"""
        if obj.qr_code:
            return format_html(
                '<img src="{}" width="50" height="50" />',
                obj.qr_code.url
            )
        return "No QR Code"
    qr_code_preview.short_description = 'QR Code'
    
    def qr_code_display(self, obj):
        """Show full QR code in detail view"""
        if obj.qr_code:
            return format_html(
                '<img src="{}" width="300" height="300" /><br><a href="{}" download>Download QR Code</a>',
                obj.qr_code.url,
                obj.qr_code.url
            )
        return "QR code will be generated automatically"
    qr_code_display.short_description = 'QR Code'
