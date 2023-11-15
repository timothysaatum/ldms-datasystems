from django.db import models
from django.contrib.auth.models import User



class CreditDB(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	db_name = models.CharField(max_length=100)
	date_created = models.DateField()


	class Meta:
		abstract=True

	def __str__(self):
		return self.user.user_name
		