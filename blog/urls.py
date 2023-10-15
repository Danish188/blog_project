from django.urls import path , include
from . import views

app_name = 'blog'

urlpatterns = [
    path('blog_list/' , views.PostList.as_view(), name = 'blog_list'),
    path('blog_detail/<int:pk_from_url>' , views.PostDetail.as_view(), name = 'blog_detail'),
]