from django.db import models

class Company(models.Model):
	
	name = models.CharField(max_length=100)
	contact = models.IntegerField()
	ad1 = models.CharField(max_length=100)
	ad2 = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	properties = models.CharField(max_length=500)


	def __str__(self):
		return self.name
