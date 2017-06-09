#coding:utf-8

from django.contrib import admin
from models import Books,Hero
# Register your models here.

class BookInfoAdmin(admin.ModelAdmin):#
    """"""
    list_display = ["title"]# hou qu models li mian de shu xing

class HeroInfoAdmin(admin.ModelAdmin):
    """"""
    list_display = ["wushu", "laohu", "xunda", "xuner", "guangyu", "zhaofei", "zhaoyun"]
# zhe li mian de zi duan yao he models li mian de zi duan bian liang yao yi yang bu ke yi chu xiang cuo wu
admin.site.register(Books, BookInfoAdmin)# zhe li shi jiang models li mian de lei he admin li mian de lei zheng he zai yi qi

admin.site.register(Hero, HeroInfoAdmin)







