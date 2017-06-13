#coding:utf-8

from django.conf.urls import url
from . import views

urlpatterns = [url("^data/$", views.data),
               url("^date/$", views.date),
               ]