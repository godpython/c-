#coding:utf-8

from django.db import models

# Create your models here.

class Info(models.Model):
    """"""
    titel = models.CharField(max_length=20)

class Knfo(models.Model):
    """"""
    nian = models.CharField(max_length=20)
    yue = models.CharField(max_length=20)

