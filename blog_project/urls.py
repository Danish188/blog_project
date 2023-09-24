from django.contrib import admin
from django.urls import path

admin.AdminSite.site_header = 'Blog Site'

urlpatterns = [
    path("admin/", admin.site.urls),
]
