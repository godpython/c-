from django.conf.urls import url
import views


urlpatterns = [
               url(r"^index/$", views.index),
               url(r"^register/$", views.register),
               url(r"^register_handle/$", views.register_handle),
               url(r"^login/$", views.login),
               url(r"^login_handle/$", views.login_handle),
               url(r"^user_center_info/$", views.user_center_info),
               url(r"^user_center_site/$", views.user_center_site),
               url(r"^detail/$", views.detail),
               url(r"^list/$", views.list),
               url(r"^qubu/$", views.qubu),
                url(r"^user_center_order/$", views.user_center_order),
               ]