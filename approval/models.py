from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Approval(models.Model):
    department = models.CharField(max_length=10)
    position = models.CharField(max_length=10)
    name = models.ForeignKey(User)
    reason = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)