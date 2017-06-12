#coding:utf-8

from django.conf.urls import url
from . import views

urlpatterns = [url(r"^index_10/$", views.index_10),
               url(r"^test2/$", views.test2),
               ]