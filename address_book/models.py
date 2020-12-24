from django.db import models

# Create your models here.
class Address(models.Model):
	names = models.CharField(max_length =200)
	email = models.EmailField(max_length =200)
	phone = models.CharField(max_length =200)
	address = models.CharField(max_length =200)
	city = models.CharField(max_length =200)
	state = models.CharField(max_length =200)
	zipcode = models.CharField(max_length =200)

	def __str__(self):
		return self.names
