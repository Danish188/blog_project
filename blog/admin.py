from django.contrib import admin
from .models import BlogPost , Category , Tag

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title' , 'author' , 'created_at' , 'updated_at')
    list_filter = ('author' , 'categories' , 'tags')
    search_fields = ('title' , 'content')
    # prepopulated_fields = {'slug':('title',)}
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Post Info' , {
            'fields':('title' , 'author' , 'categories', 'tags' , 'content')
        }),
    )
