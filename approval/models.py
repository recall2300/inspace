from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils import timezone


class EmployeeManager(BaseUserManager):
    def create_user(self, email, username, image=None, gender=None, nickname=None, department=None, position=None,
                    contact=None, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            department=department,
            position=position,
            contact=contact,
            image=image,
            gender=gender,
            nickname=nickname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, image, gender, nickname, username, department, position, contact, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email=email,
            password=password,
            username=username,
            department=department,
            position=position,
            contact=contact,
            image=image,
            gender=gender,
            nickname=nickname,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Employee(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    image = models.ImageField('profile picture', upload_to='static/images/profile/', null=True, blank=True)
    nickname = models.CharField(max_length=30, null=True)
    GENDER = (
        ('male', '남자'),
        ('female', '여자'),
    )
    gender = models.CharField(max_length=6, choices=GENDER, null=True)
    username = models.CharField(max_length=20, help_text='Is this user account activated?')
    department = models.CharField(max_length=10, null=True)
    position = models.CharField(max_length=10, null=True)
    contact = models.CharField(max_length=11, null=True)
    signature_image = models.ImageField(
        null=True,
        blank=True,
        upload_to='static/signature/'
    )

    is_active = models.BooleanField(default=True, help_text='Is this user account activated?')
    is_admin = models.BooleanField(default=False)

    objects = EmployeeManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'department', 'position', 'contact']

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __str__(self):  # __unicode__ on Python 2
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Approval(models.Model):
    department = models.CharField(max_length=10)
    position = models.CharField(max_length=10)
    # username = models.ForeignKey(settings.AUTH_USER_MODEL)
    username = models.CharField(max_length=10)
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
        return str(self.id)


class Comment(models.Model):
    approval = models.ForeignKey(Approval)
    employee = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField(null=False)
    write_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.approval.id
