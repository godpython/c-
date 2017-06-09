#coding:utf-8

from django.contrib import admin
from models import *
# Register your models here.


class TypeInfoAdmin(admin.ModelAdmin):
    """"""
    list_display = ["id", "title"]

class GoodsInfoAdmin(admin.ModelAdmin):
    """"""
    list_per_page = 15
    list_display = ["id", "gtitle", "gprice", "gunit","gclick",
                    "gkucun", "gtype"]





admin.site.register(TypeInof, TypeInfoAdmin)
admin.site.register(GoodsInfo, GoodsInfoAdmin)