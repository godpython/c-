from django.conf.urls import url

import views

urlpatterns = [url(r"^index/$", views.index),
               url(r"^register/$", views.register),
               # url(r"^login_3/$", views.login_3),
               ]