from django.db import models

from user.models import User

# Create your models here.
class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bloodgroup = models.CharField(max_length=5)
    age = models.IntegerField()
