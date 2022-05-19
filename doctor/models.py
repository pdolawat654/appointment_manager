from django.db import models

from user.models import User

# Create your models here.
class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hospital = models.CharField(max_length=50)
    department = models.CharField(max_length=50)