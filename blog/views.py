from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Category
from django.views import View
from .models import BlogPost , Category
from django.views import View
from .form import BlogCreateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

class PostList(View):
    def get(self , request):
        data = BlogPost.objects.all()
        return render(request , 'blog/blog_list.html' , {'posts':data})

class PostDetail(View):
    def get(self , request , pk_from_url):
        data = BlogPost.objects.get(pk = pk_from_url)
        return render(request , 'blog/blog_detail.html' , {'posts':data} )
    
class PostCreate(LoginRequiredMixin , CreateView):
    model = BlogPost
    form_class = BlogCreateView
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class CatCreate(LoginRequiredMixin , CreateView):
    model = Category
    fields = '__all__'
    
class PostUpdate(LoginRequiredMixin , UpdateView):
    model = BlogPost
    form_class = BlogCreateView
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        
        return super().form_valid(form)

class PostDelete(DeleteView):
    model = BlogPost
