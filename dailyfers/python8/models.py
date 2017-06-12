from django.db import models

# Create your models here.

class Info(models.Model):
    """"""
    title = models.CharField(max_length=20)

class Font(models.Model):
    """"""
    xunda = models.CharField(max_length=20)
    xuner = models.CharField(max_length=20)
