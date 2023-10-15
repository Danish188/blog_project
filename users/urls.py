from django.urls import path , include
from . import views

app_name = 'users'

urlpatterns = [
    path('register/' , views.register , name = 'register'),
    path('logout/' , views.logout , name = 'logout'),
    path('' , views.login , name = 'login'),
]