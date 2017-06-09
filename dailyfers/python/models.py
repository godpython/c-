#coding:utf-8

from django.db import models
from tinymce.models import HTMLField

class UserInfo(models.Model):
    """"""
    uanme = models.CharField(max_length=20)# yong hu ming
    upwd = models.CharField(max_length=40)# mi ma
    uemail = models.CharField(max_length=30)# you xiang
    ushou = models.CharField(max_length=20, default="")
    uaddress = models.CharField(max_length=100, default="")
    uyoubian = models.CharField(max_length=6, default="")
    uphone = models.CharField(max_length=11, default="")


class TypeInof(models.Model):
    """"""
    title = models.CharField(max_length=20)# shang bing de ming zi fe chuang du

    def __str__(self):
        return self.title.encode("utf-8")

class GoodsInfo(models.Model):
    """"""
    gtitle = models.CharField(max_length=100)# shang bing de ming zi
    gprice = models.DecimalField(max_digits=5, decimal_places=2)# shang bing de jia ge
    gpic = models.ImageField(upload_to="goods")# shang bing de tu bian
    gtype = models.ForeignKey("TypeInof")# sheng zhi de wei jian
    gjianjie = models.CharField(max_length=200)
    gunit = models.CharField(max_length=50)
    gjieshao = HTMLField()# fu wen ping bian yi qi
    gclick = models.IntegerField(default=0)# ren qi lei xing
    gkucun = models.IntegerField(default=1000)# ku zhu liang



    def __str__(self):
        return self.title.encode("utf-8")