from django.db import models

# Create your models here.

class Books(models.Model):
    """"""
    title = models.CharField(max_length=20)
    isdelete = models.CharField(max_length=20)

class Cooks(models.Model):
    """"""
    xunda = models.CharField(max_length=20)
    xuner = models.CharField(max_length=30)

    zhaofei = models.CharField(max_length=20)
    zhaoxun = models.CharField(max_length=20)
    zhaozilong = models.CharField(max_length=20)


