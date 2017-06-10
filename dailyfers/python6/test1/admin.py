#coding:utf-8

from django.contrib import admin
from models import Inof,Books
# Register your models here.


class Cooks(admin.ModelAdmin):
    """"""
    list_display = ["title"]


class Dooks(admin.ModelAdmin):
    """"""
    list_display = ["guanyu", "zhafei", "zilong", "xuda", "xuer"]


admin.site.register(Inof,Cooks)
admin.site.register(Books, Dooks)

