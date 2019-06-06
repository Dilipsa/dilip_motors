from django.db import models
from django.conf import settings

class Car(models.Model):
    car_id = models.CharField(max_length=20)
    car_name = models.CharField(max_length=20)
    car_variant = models.CharField(max_length=20)
    car_fuel = models.CharField(max_length=20)
    car_color = models.CharField(max_length=20)

    def __str___(self):
        return self.c_name
