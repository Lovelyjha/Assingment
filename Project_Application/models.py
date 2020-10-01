from django.db import models

# Create your models here.
class Manager(models.Model):
    email=models.EmailField(max_length=70)
    firstname=models.CharField(max_length=64)
    lastname=models.CharField(max_length=64)
    password=models.CharField(max_length=50)
    address=models.CharField(max_length=256)
    dateofbirth=models.DateField(max_length=8)
    company=models.CharField(max_length=256)
