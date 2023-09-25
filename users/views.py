from django.shortcuts import render , redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() 
            auth_login(request , user) 
            return redirect('blog:home')
    else:
        form = UserCreationForm() 
    return render(request , 'users/register.html' , {'form' : form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            auth_login(request , form.get_user())
            return redirect('blog:home')
    else:
        form = AuthenticationForm(request)
    return render(request , 'users/login.html' , {'form':form})
