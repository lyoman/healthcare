from django.utils import timezone
from django.contrib.auth.models import Permission
from django.db import models
from django.conf import settings


APPROVE_CHOICES = (
    ("Pending", "Pending"),
    ("Rejected", "Rejected"),
    ("Approved", "Approved"),
)

class Approval(models.Model):
    user 		   = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE, related_name='logged_in_user')
    status         = models.CharField(default="Pending", choices=APPROVE_CHOICES, max_length=10)
    approvedby     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null = True, blank = True, related_name='admin_approving_request')
    updated        = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp      = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.status

    class Meta:
        ordering = ["-timestamp", "-updated"]