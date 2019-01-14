from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Residence(models.Model):

	user = models.CharField(max_length=80)
	antenna = models.CharField(max_length=15)
	lat = models.DecimalField(max_digits=48,decimal_places=40,default=0.1)
	lon = models.DecimalField(max_digits=48,decimal_places=40,default=0.1)
	city = models.CharField(max_length=50, default=" ")

	def __str__(self):

		return self.user+","+self.antenna+","+self.lat+","+self.lon+","+self.city

class UserAntenna(models.Model):

	antenna = models.CharField(max_length=15) 
	user = models.CharField(max_length=80)

	def __str__(self):

		return self.antenna+","+self.user