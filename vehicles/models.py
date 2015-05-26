from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class Owner(models.Model):
    id_number = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=50)
    created = models.DateField(default=timezone.now)

    def validate_id_number(self):
        if self.id_number == '12345':
            msg = "Person is not allowed to own a car in Kenya"
            raise ValidationError(msg)

    def clean(self):
        self.validate_id_number()

    def save(self, *args, **kwargs):
        self.clean()
        super(Owner, self).save(*args, **kwargs)


class Vehicle(models.Model):
    created = models.DateField(default=timezone.now)
    number_plate = models.CharField(max_length=200)
    make = models.CharField(max_length=100)
    owner = models.ForeignKey(Owner)
