from django.contrib import admin
<<<<<<< HEAD
from .models import BlogPost , Category , Tag
=======
from .models import BlogPost , Category
>>>>>>> post-creation

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
<<<<<<< HEAD

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
=======
>>>>>>> post-creation
    
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title' , 'author' , 'created_at' , 'updated_at')
<<<<<<< HEAD
    list_filter = ('author' , 'categories' , 'tags')
    search_fields = ('title' , 'content')
    # prepopulated_fields = {'slug':('title',)}
=======
    list_filter = ('author' , 'categories')
    search_fields = ('title' , 'content')
>>>>>>> post-creation
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Post Info' , {
<<<<<<< HEAD
            'fields':('title' , 'author' , 'categories', 'tags' , 'content')
=======
            'fields':('title' , 'author' , 'categories' , 'content')
>>>>>>> post-creation
        }),
    )
