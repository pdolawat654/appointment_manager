from random import randint
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length = 20)
    verified = models.BooleanField(default=False)
    otp = models.IntegerField(null = True)
    phone = models.CharField(max_length=13)