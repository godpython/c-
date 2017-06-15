#coding:utf-8

from django.db import models

# Create your models here.

class Info(models.Model):
    """"""
    title = models.CharField(max_length=20)

class Fnfo(models.Model):
    """"""
    lijiang = models.CharField(max_length=20)
    gaung = models.CharField(max_length=20)

