from django.db import models
from django.utils import timezone

class Employee_detail(models.Model):
    name=models.CharField(max_length=50)
    id=models.CharField(primary_key=True,max_length=10)
    salary=models.FloatField()
    department=models.CharField(max_length=50)
    gender=models.CharField(max_length=20)
    joined=models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name
