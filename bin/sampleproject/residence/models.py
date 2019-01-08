from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Residence(models.Model):
	user = models.CharField(max_length=100)
	antenna = models.CharField(max_length=100)


class UserAntenna(models.Model):
	antenna = models.CharField(max_length=100) 
	user = models.CharField(max_length=100)
