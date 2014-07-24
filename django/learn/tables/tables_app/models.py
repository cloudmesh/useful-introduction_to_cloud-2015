from django.db import models
import django_tables2 as tables

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=200)
