from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.
class User(AbstractUser):
    medicall_staffer = models.CharField(max_length=50, blank=True)
    specialist_area = models.CharField(max_length=50, blank=True)
    email           = models.EmailField(unique=True, blank=True)
    last_name       = models.CharField(blank=True, max_length=255)
    first_name      = models.CharField(blank=True, max_length=255)
    phone_regex     = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number    = models.CharField(max_length=17, blank=True) # validators should be a list
    updated         = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp       = models.DateTimeField(auto_now=False, auto_now_add=True)


    def  __str__(self):
        return self.username
    
    class Meta:
        ordering = ["-timestamp", "-updated"]
