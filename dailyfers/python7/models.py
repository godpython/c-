from django.db import models

# Create your models here.

class Inof(models.Model):
    """"""
    ititle = models.CharField(max_length=20)

class Fnof(models.Model):
    """"""
    guanyu = models.CharField(max_length=20)

    zhangfei = models.CharField(max_length=20)

    zilong = models.CharField(max_length=20)
