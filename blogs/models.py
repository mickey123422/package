from django.db import models

# Create your models here.


class Post(models.Model):
    name=models.CharField(max_length=50)
    line=models.CharField(max_length=50)
    phone=models.IntegerField()
    address=models.TextField(max_length=200)



