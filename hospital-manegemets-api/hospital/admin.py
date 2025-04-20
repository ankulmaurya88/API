from django.contrib import admin
from .models import Doctors, Patients, Appointments, MediflowDoctor, MediflowPatient, MediflowAppointment

# If you're using a custom admin class, register the model like this:
class MediflowDoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'specialization', 'phone', 'availability', 'department')
    search_fields = ('specialization', 'phone')

# Only register once, either using @admin.register or admin.site.register
@admin.register(MediflowDoctor)
class MediflowDoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'specialization', 'phone', 'availability', 'department')
    search_fields = ('specialization', 'phone')

# Register the other models as usual
admin.site.register(Doctors)
admin.site.register(Patients)
admin.site.register(Appointments)
