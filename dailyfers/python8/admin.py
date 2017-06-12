#coding:utf-8


from django.contrib import admin
from models import Info, Font
# Register your models here.

class Date(admin.ModelAdmin):
    """"""
    list_display = ["title"]

class Eate(admin.ModelAdmin):
    """"""
    list_display = ["xunda", "xuner"]

admin.site.register(Info, Date)
admin.site.register(Font, Eate)