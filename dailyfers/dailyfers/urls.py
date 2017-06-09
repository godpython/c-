from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r"admin/", include(admin.site.urls)),
    url(r"^user/", include("python.urls")),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r"^user_/", include("python2.urls")),
    url(r"^", include("python5.urls")),
]

