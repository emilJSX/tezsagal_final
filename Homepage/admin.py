from django.contrib import admin
from .models import Doctor, Patient, Appointment
# Register your models here.

class DoctorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Doctor, DoctorAdmin)

class PatientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patient, PatientAdmin)
admin.site.register(Appointment)
