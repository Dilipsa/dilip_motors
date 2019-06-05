from django.db import models
from django.utils import timezone

class Branch(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    manager=models.CharField(max_length=50)
    opened=models.DateTimeField()

    def __str__(self):
        return self.name
