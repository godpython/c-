#coding:utf-8

from django.contrib import admin
from models import Books, Bookc
# Register your models here.

class Info(admin.ModelAdmin):
    """"""
    list_display = ["title"]

class Font(admin.ModelAdmin):
    """"""
    list_display = ["zhangfei", "guangyu", "zilong"]


admin.site.register(Books, Info)

admin.site.register(Bookc, Font)
