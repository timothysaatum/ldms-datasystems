from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone





class Delivery(models.Model):
	date_created = models.DateField(default=timezone.now)
	created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=200)
	contact = models.CharField(max_length=15)
	email = models.EmailField()
	digital_address = models.CharField(max_length=10)
	website = models.URLField()

	def __str__(self):
		return self.name


class DeliveryServices(models.Model):
	added_on = models.DateField(default=timezone.now)
	created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
	name_of_service = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=20, decimal_places=2)
	

	def __str__(self):
		return self.name_of_service
