<<<<<<< HEAD
from django.urls import path , reverse_lazy
=======
from django.urls import path , include
>>>>>>> 5ea4624c3c558002bf338556f84e06be63755c79
from . import views

app_name = 'blog'

urlpatterns = [
<<<<<<< HEAD
    path('' , views.PostList.as_view(), name = 'blog_list'),
    path('<int:pk_from_url>/detail' , views.PostDetail.as_view(), name = 'blog_detail'),
    path('blog_create/' ,
        views.PostCreate.as_view(success_url = reverse_lazy('blog:blog_list')), name = 'blog_create'),
    path('cat_create/' ,
        views.CatCreate.as_view(success_url = reverse_lazy('blog:blog_create')), name = 'cat_create'),
    path('<int:pk>/delete', 
        views.PostDelete.as_view(success_url=reverse_lazy('blog:blog_list')), name='blog_delete'),
    path('<int:pk>/update', 
        views.PostUpdate.as_view(success_url=reverse_lazy('blog:blog_list')), name='blog_Update'),
=======
    path('blog_list/' , views.PostList.as_view(), name = 'blog_list'),
    path('blog_detail/<int:pk_from_url>' , views.PostDetail.as_view(), name = 'blog_detail'),
>>>>>>> 5ea4624c3c558002bf338556f84e06be63755c79
]