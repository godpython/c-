#coding:utf-8
from django.contrib import admin
from models import Info,Knfo
# Register your models here.

class Wps(admin.ModelAdmin):
    """"""
    list_display = ["titel"]


class Offce(admin.ModelAdmin):
    """"""
    list_display = ["nian", "yue"]


admin.site.register(Info, Wps)
admin.site.register(Knfo, Offce)
