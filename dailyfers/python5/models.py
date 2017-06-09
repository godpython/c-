from django.db import models

# Create your models here.

class Books(models.Model):
    """"""
    title = models.CharField(max_length=20)
    isdelete = models.CharField(max_length=20)

class Bookc(models.Model):
    """"""
    zhangfei = models.CharField(max_length=20)
    guangyu = models.CharField(max_length=20)
    zilong = models.CharField(max_length=20)
    key = models.ForeignKey("Books")


