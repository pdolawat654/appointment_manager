from statistics import mode
from django.db import models
from doctor.models import Doctor

from patient.models import Patient

# Create your models here.
class Appointment(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
