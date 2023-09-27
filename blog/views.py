from django.shortcuts import render , get_object_or_404
from .models import BlogPost , Tag , Category
from django.views import View

class PostList(View):
    def get(self , request):
        data = BlogPost.objects.all()
        return render(request , 'blog/blog_list.html' , {'posts':data})

class PostDetail(View):
    def get(self , request , pk_from_url):
        data = BlogPost.objects.get(pk = pk_from_url)
        return render(request , 'blog/blog_detail.html' , {'posts':data} )
