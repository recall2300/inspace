from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Approval(models.Model):
    department = models.CharField(max_length=10)
    position = models.CharField(max_length=10)
    name = models.ForeignKey(User)
    reason = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    write_date = models.DateTimeField(default=timezone.now)
    LEAVE_CLASSIFICATION_CHOICES = (
        ('연차', '연차'),
        ('오전반차', '오전반차'),
        ('오후반차', '오후반차'),
        ('병가', '병가'),
        ('경조사휴가', '경조사휴가'),
        ('산전후휴가', '산전후휴가'),
        ('기타', '기타')
    )
    leave_classification = models.CharField(max_length=5, choices=LEAVE_CLASSIFICATION_CHOICES, default='연차')
    emergency_contact = models.CharField(max_length=11)
    destination = models.CharField(max_length=30)
    comments = models.PositiveSmallIntegerField(default=0, null=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    email = models.CharField(max_length=30)
    name = models.CharField(max_length=5)
    department = models.CharField(max_length=10)
    position = models.CharField(max_length=10)
    contact = models.CharField(max_length=11)
    signature_file = models.FileField(upload_to='uploads/%Y/%m/%d/')

    def __str__(self):
        return self.name


class Comment(models.Model):
    approval = models.ForeignKey(Approval)
    employee = models.ForeignKey(Employee)
    content = models.TextField(null=False)
    write_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.approval_number
