from django.db import models
from laboratories.models import Lab, Test
from hospitals.models import Hospital
import uuid



class Patient(models.Model):

	HEALTHY_INSUARANCE_TYPE = [
		('NHIS', 'NHIS'),
		('Premium', 'Premium')
	]

	name = models.CharField(max_length=100)
	hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
	laboratory = models.ForeignKey(Lab, on_delete=models.CASCADE)
	age = models.PositiveSmallIntegerField()
	tests = models.ManyToManyField(Test, blank=True)
	health_insuarance_type = models.CharField(max_length=100, choices=HEALTHY_INSUARANCE_TYPE)
	slug = models.UUIDField(default=uuid.uuid64, editable=False)


	def __str__(self):
		return f'{self.namef}@{self.hospital}'
	