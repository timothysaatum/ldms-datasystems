from django.contrib import admin
from .models import Patient


#registration of patient models to allow for viewing and editing at the admin interface
class PatientAdmin(admin.ModelAdmin):
	list_display = ('name', 'hospital', 'laboratory', 'age')


	def get_patient(self, obj):
		return [patient.tests for patient in obj.tests.all()]


admin.site.register(Patient, PatientAdmin)