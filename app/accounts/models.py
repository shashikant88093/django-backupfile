from django.db import models
# from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.utils import timezone


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    # email = models.EmailField(verbose_name='email',max_length=255)
    # phone = models.CharField(null=True,max_length=255)
    REQUIRED_FIELDS = [
        'email',
        # 'phone',
        # 'first_name',
        # 'last_name'
    ]
    # USERNAME_FIELD = 'email'

    def get_username(self):
        return self.username


class Table(models.Model):
    # username = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    Run_ID = models.CharField(max_length=120)
    Date_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    Run_status = models.TextField()
    count = models.IntegerField()
    path = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.Run_ID)
