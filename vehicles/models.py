from django.db import models
from django.utils import timezone


class Owner(models.Model):
    id_number = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=50)
    created = models.DateField(default=timezone.now)


class Vehicle(models.Model):
    created = models.DateField(default=timezone.now)
    number_plate = models.CharField(max_length=200)
    make = models.CharField(max_length=100)
    owner = models.ForeignKey(Owner)
