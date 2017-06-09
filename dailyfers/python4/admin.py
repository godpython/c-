#coding:utf=8

from django.contrib import admin
from models import Books, Cooks
# Register your models here.

class Info(admin.ModelAdmin):
    """"""
    list_display = ["title"]

class Font(admin.ModelAdmin):
    """"""
    list_display = ["xunda", "xuner", "zhaofei", "zhaoxun", "zhaozilong"]

admin.site.register(Books, Info)
admin.site.register(Cooks, Font)