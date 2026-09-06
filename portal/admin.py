from django.contrib import admin
from .models import Patient, Appointment, LabResult

# 1. Register Patient
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'dob', 'phone')
    search_fields = ('name',)

# 2. Register Appointment
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'service', 'date', 'status')
    list_filter = ('status', 'date')

# 3. Register LabResult
@admin.register(LabResult)
class LabResultAdmin(admin.ModelAdmin):
    list_display = ('patient', 'test_name', 'result_value', 'status')
    list_filter = ('status',)