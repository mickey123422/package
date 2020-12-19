from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.


class profiles(models.Model):
    user_id = models.OneToOneField(
        User, on_delete=models.CASCADE)
    storename = models.CharField(max_length=50, null=True)
    storephone = models.CharField(max_length=50, null=True)
    storeaddress = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)


class Post(models.Model):
    def as_bootstrap_status(self):
        if self.status == 'picked up':
            return 'info'
        elif self.status == 'pending':
            return 'warning'
        elif self.status == 'delivered':
            return 'success'
    name = models.CharField(max_length=50, null=True)
    line = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    address = models.TextField(max_length=200, null=True)
    packname = models.CharField(max_length=50, default='Unknow')
    createdate = models.DateTimeField(default=now, editable=False)
    status = models.CharField(
        max_length=50,)
    size = models.CharField(
        max_length=50,  null=True)
    types = models.CharField(
        max_length=50, )
    sensorid = models.CharField(
        max_length=50)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)


class Pack(models.Model):
    trackingno = models.CharField(max_length=50)
    size = models.CharField(max_length=10)
    phone = models.IntegerField()
    address = models.TextField(max_length=200)


class esp8266(models.Model):
    vibration = models.IntegerField()
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    day = models.CharField(max_length=100)
