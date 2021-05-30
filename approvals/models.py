from django.utils import timezone
from django.contrib.auth.models import Permission
from django.db import models
from django.conf import settings

class Approval(models.Model):
    user 		   = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    status         = models.CharField(default="pending")
    approvedby     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null = True, blank = True)
    updated        = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp      = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.status

    class Meta:
        ordering = ["-timestamp", "-updated"]