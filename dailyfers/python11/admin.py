#coding:utf-8

from django.contrib import admin
from models import Info,Fnfo
# Register your models here.

class Dates(admin.ModelAdmin):
    """"""
    list_display = ["title"]

class And(admin.ModelAdmin):
    """"""
    list_display = ["lijiang", "gaung"]

admin.site.register(Info, Dates)
admin.site.register(Fnfo, And)



