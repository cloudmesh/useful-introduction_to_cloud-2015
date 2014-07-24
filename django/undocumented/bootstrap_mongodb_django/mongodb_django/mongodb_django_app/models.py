from django.db import models

# Create your models here.

class Person (models.Model):
	name = models.CharField(verbose_name = "full name",
		                max_length = 120)
