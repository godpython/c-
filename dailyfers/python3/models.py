#coding:utf-8

from django.db import models

# Create your models here.

class Boosk(models.Model):
    """"""
    title = models.CharField(max_length=20)
    isdelete = models.CharField(max_length=30)

class Coosk(models.Model):
    """"""
    zhaofei = models.CharField(max_length=20)
    guangyu = models.CharField(max_length=20)
    zilong = models.CharField(max_length=20)

    xunda = models.CharField(max_length=20)
    xuner = models.CharField(max_length=20)




