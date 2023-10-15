from django import forms
from .models import BlogPost , Category

choice = Category.objects.all().values_list('name','name')
choice_list = []

for i in choice:
    choice_list.append(i)


class BlogCreateView(forms.ModelForm):    
    class Meta:
        model = BlogPost
        fields = ['title' , 'content' , 'categories']
        
        widgets = {
            'categories':forms.Select(choices=choice_list , attrs={'class':'form-control'}),
        }
        
        