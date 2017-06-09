#coding:utf-8

from django.db import models

class Books(models.Model):# ding yi zi duan zhe ge lei ji cheng yu models.Model lei xing
    """tu shu lei """
    title = models.CharField(max_length=20)# ding yi zi duan
    isdelete = models.IntegerField(default=0)

class Hero(models.Model):
    """ying xun lei """
    wushu = models.CharField(max_length=20)
    laohu = models.CharField(max_length=20)

    xunda = models.CharField(max_length=20)
    xuner = models.CharField(max_length=20)

    guangyu = models.CharField(max_length=20)
    zhaofei = models.CharField(max_length=20)
    zhaoyun = models.CharField(max_length=20)
    key = models.ForeignKey("Books")# zhe li ding yi de shi zi duan ke yi tong zhe ge wei jian lai fang wen tu shu
    # tu shu ye yi tong guo zhe ge wei jian lai fang wen quan bu de ying xun