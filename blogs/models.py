from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
# Create your models here.


class Post(models.Model):
    name = models.CharField(max_length=50, null=True)
    line = models.CharField(max_length=50, null=True)
    phone = models.IntegerField(null=True)
    address = models.TextField(max_length=200, null=True)
    packname = models.CharField(max_length=50, default='Unknow')
    createdate = models.DateTimeField(default=now, editable=False)
    status = models.CharField(
        max_length=50, default='Order has been successfully picked up')
    size = models.CharField(
        max_length=50, default='S')
    types = models.CharField(
        max_length=50, default='Unknow')
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)


class Pack(models.Model):
    trackingno = models.CharField(max_length=50)
    size = models.CharField(max_length=10)
    phone = models.IntegerField()
    address = models.TextField(max_length=200)
