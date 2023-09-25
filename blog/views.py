from django.shortcuts import render , HttpResponse

def home(request):
    return HttpResponse('<h1>This is Home Page</h1>')