from django.contrib import admin
from django.urls import path , include

admin.AdminSite.site_header = 'Blog Site'

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/" , include('blog.urls')),
    path("" , include('users.urls')),
]
