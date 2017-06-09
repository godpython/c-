#coding:utf-8

from django.contrib import admin
from models import Boosk, Coosk
# Register your models here.

class Info(admin.ModelAdmin):
    """guan li shu ju """
    list_display = ["title"]

class Font(admin.ModelAdmin):
    """guan li shu ju """
    list_display = ["zhaofei", "guangyu", "zilong", "xunda", "xuner"]

admin.site.register(Boosk, Info)
admin.site.register(Coosk, Font)


