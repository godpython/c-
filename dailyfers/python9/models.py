from django.db import models

# Create your models here.

class Info(models.Model):
    """"""
    title = models.CharField(max_length=20)


class Kofo(models.Model):
    """"""
    ziyu = models.CharField(max_length=20)
    zilong = models.CharField(max_length=20)

