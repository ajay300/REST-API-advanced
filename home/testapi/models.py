from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=24)
    phone = models.IntegerField()
    emp_id = models.IntegerField(null=True)
    email = models.CharField(max_length=30)
    location = models.CharField(max_length=23)

