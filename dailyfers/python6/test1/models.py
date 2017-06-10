from django.db import models

# Create your models here.


class Inof(models.Model):
    """"""
    title = models.CharField(max_length=20)
    date = models.DateField()

class Books(models.Model):
    """"""
    guanyu = models.CharField(max_length=20)
    zhafei = models.CharField(max_length=20)
    zilong = models.CharField(max_length=20)

    xuda = models.CharField(max_length=20)
    xuer = models.CharField(max_length=20)

    key = models.ForeignKey("Inof")# SHE ZHI WEI JIANG


