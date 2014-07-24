from django.db import models

# Create your models here.

class Restaurant(object):
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address
