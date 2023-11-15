from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from deliveries.models import Delivery
import secrets
import math
import uuid
#from hospitals.models import Hospital





'''
A model for creating a laboratory, which includes the fields user so as to enable us

filter the laboratories in the data base according the users in our system

This allows for custom user interface display of data
'''
class Lab(models.Model):

	logo = models.ImageField(upload_to='labs/logos')
	created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	created_on = models.DateField(default=timezone.now)
	lab_name = models.CharField(max_length=100)
	acreditation_code = models.CharField(max_length=150)
	digital_address = models.CharField(max_length=200)
	region_of_location = models.CharField(max_length=50)
	telephone = models.CharField(max_length=30)
	email_address = models.EmailField()
	website = models.URLField(null=True)
	subscription_duration = models.DateField(null=True, blank=True)
	is_acredited = models.BooleanField(default=False)
	subscribe_for_premium = models.BooleanField(default=False)
	subscription_key = models.CharField(max_length=10)
	slug = models.UUIDField(default=uuid.uuid64, editable=False)


	def __str__(self):
		return self.lab_name


	def add_badge(self):

		badge_icon = 'fa-solid fa-certificate'

		return badge_icon


	def check_acreditation_status(self):

		if self.acreditation_code is not None:

			self.is_acredited = True
			self.is_acredited.save()

			return self.is_acredited

		else:
			self.is_acredited = False
			return self.is_acredited



	def save(self, *args, **kwargs):

		if self.subscribe_for_premium != False:
			while not self.subscription_key:

				subscription_key = secrets.token_urlsafe(10)
				object_with_similar_ref = Lab.objects.filter(subscription_key=subscription_key)

				if not object_with_similar_ref:
					self.subscription_key = subscription_key

		super().save(*args, **kwargs)


	def get_absolute_url(self):
		return reverse('/', kwargs={'pk': self.pk})



'''
A model for creating a department within a laboratory, this includes the head's name
contact and email address
'''
class Department(models.Model):
	department_name = models.CharField(max_length=150)
	laboratory = models.ForeignKey(Lab, on_delete=models.CASCADE)
	department_head = models.CharField(max_length=200)
	contact = models.CharField(max_length=15)
	email_address = models.EmailField()
	tests_scope = models.ManyToManyField('Test', blank=True)
	slug = models.UUIDField(default=uuid.uuid64, editable=False)

	def __str__(self):
		return self.department_name



	def get_absolute_url(self):
		return reverse('/', kwargs={'pk': self.pk})

 
'''
A model for adding the test that a laboratory does. It will be displayed as a formset to add for multiple creation

of tests on the same page.
'''
class Test(models.Model):
	department_name = models.ForeignKey(Department, on_delete=models.CASCADE)
	date_added = models.DateField(default=timezone.now)
	test_name = models.CharField(max_length=1500)
	price = models.DecimalField(max_digits=20, decimal_places=2)
	discount = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
	apply_discount = models.BooleanField(default=False)
	slug = models.UUIDField(default=uuid.uuid64, editable=False)


	def __str__(self):
		return self.test_name



	#calculating the percentage discount a user gets base on the dicount amount given
	
	def percentage_discount(self):

		if self.discount != None:

			discount_percent = math.ceil((self.discount / self.price) * 100)

			return f'{discount_percent}%'

		return f'0%'



	def is_discount(self):

		if self.apply_discount == True:

			return 'discounted'

		return 'not discounted'


	def get_absolute_url(self):
		return reverse('/', kwargs={'pk': self.pk})





'''
A model for submitting test results from a laboratory to a hospital after it is done testing
'''
class TestResultsPdf(models.Model):

	submitted_on = models.DateField(default=timezone.now)
	laboratory = models.ForeignKey(Lab, on_delete=models.CASCADE)
	send_by = models.CharField(max_length=200)
	send_to = models.CharField(max_length=150)
	test = models.ForeignKey(Test, on_delete=models.CASCADE)
	is_verified = models.BooleanField(default=False)
	upload_pdf = models.FileField(upload_to='labs/tests/results', blank=True, null=False)
	slug = models.UUIDField(default=uuid.uuid64, editable=False)
	

	def __str__(self):
		return self.test.test_name


	def very_test(self):
		if self.upload_pdf != None:
			self.is_verified = True
		self.is_verified = False
		self.is_verified

		return self.is_verified


	def get_absolute_url(self):
		return reverse('result-detail', kwargs={'pk': self.pk})


class Other(models.Model):
	pass



'''
Defining a base model for all laboratory tests results, this will be inherited by other 
sub results parameters.
'''
class Results(models.Model):

	test = models.ForeignKey(Test, on_delete=models.CASCADE)
	date_added = models.DateField(default=timezone.now)
	date_modified = models.DateField(default=timezone.now)
	is_verified = models.BooleanField(default=False)
	is_paid_for = models.BooleanField(default=False)
	send_result = models.BooleanField(default=False)
	

	class Meta:
		abstract=True