from django.utils import timezone
from django.contrib.auth.models import Permission
from django.db import models
from django.conf import settings

class Patient(models.Model):
    user 		   = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    patient_name   = models.CharField(max_length=250)
    patient_id     = models.CharField(max_length=200)
    # store_logo     = models.ImageField(upload_to='store_logo/')
    patient_history = models.TextField(blank = True)
    heart_rate	   = models.CharField(max_length=200)
    recommended_diagnosis = models.CharField(max_length=500, blank = True)
    respiratory_rate = models.CharField(max_length=200)
    temperature	   = models.CharField(max_length=200)
    blood_pressure = models.CharField(max_length=200)
    active         = models.BooleanField(default=True)
    updated        = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp      = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.patient_id + ' - ' + self.patient_name

    class Meta:
        ordering = ["-timestamp", "-updated"]