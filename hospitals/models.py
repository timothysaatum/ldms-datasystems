from django.db import models
from django.contrib.auth.models import User
from laboratories.models import Lab, Test
from django.utils import timezone
from deliveries.models import Delivery
import uuid
import base



'''
A model that defines the blueprint for created and update a hospital
according to the paramaeters provided
'''
class Hospital(models.Model):
	created_by = models.ForeignKey(User, on_delete=models.CASCADE)
	created_on = models.DateField(default=timezone.now)
	hospital_name = models.CharField(max_length=200)
	acreditation_code = models.CharField(max_length=150)
	logo = models.ImageField(upload_to='hospitals/logos')
	digital_address = models.CharField(max_length=200)
	region_of_location = models.CharField(max_length=50)
	telephone = models.CharField(max_length=30)
	email_address = models.EmailField()
	website = models.URLField()
	slug = models.UUIDField(default=uuid.uuid64, editable=False)


	def __str__(self):
		return self.hospital_name

	def is_acredited(self):
		if self.acreditation_code != None:
			return True
		return False

	def add_badge(self):
		
		badge_icon = 'fa-solid fa-certificate'

		return badge



class Ward(models.Model):
	ward_name = models.CharField(max_length=150)
	hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
	head_of_ward = models.CharField(max_length=100)
	contact  = models.CharField(max_length=15)
	email_address = models.EmailField()
	slug = models.UUIDField(default=uuid.uuid64, editable=False)


	def __str__(self):
		return self.ward_name


class Sample(models.Model):

	SEX = [
		('Male', 'Male'),
		('Female', 'Female')
	]
	
	generated_on = models.DateField(default=timezone.now)
	ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
	send_to = models.ForeignKey(Lab, on_delete=models.CASCADE)
	send_by = models.CharField(max_length=200)
	phone = models.CharField(max_length=15)
	sample_type = models.CharField(max_length=200)
	sample_tube = models.CharField(max_length=50)
	sample_id = models.CharField(max_length=100)
	sample_origin = models.CharField(max_length=100)
	sex_of_client = models.CharField(max_length=10, choices=SEX)
	name_of_client = models.CharField(max_length=100)
	age_of_client = models.CharField(max_length=10)
	department = models.CharField(max_length=100)
	test_to_be_done = models.ManyToManyField(Test)
	delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
	received_by = models.CharField(max_length=150)
	is_delivered = models.BooleanField(default=False)
	slug = models.UUIDField(default=uuid.uuid64, editable=False)


	def __str__(self):
		return f'{self.sample_id} -- {self.name_of_client}'

	
	def hospital(self):
		return self.ward.hospital.hospital_name

	
	def get_laboratory(self):
		return self.send_to.lab_name



'''
Table for giving discounted to users based on the number of times they have used our servcie
This has inherited from the base CreditDB model
'''
class HospitalCredit(base.CreditDB):

	is_credited = models.BooleanField(default=True)