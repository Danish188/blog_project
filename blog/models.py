from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self) -> str:
        return self.name

<<<<<<< HEAD
class Tag(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self) -> str:
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)
=======
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    categories = models.CharField(max_length=200 , default='undefined')
>>>>>>> post-creation
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title