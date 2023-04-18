from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return home(request)

def home(request):
    return render(request, 'home.html')

def courses(request):
    return render(request, 'courses.html')

def signup(request):
    return render(request, 'signup.html') 

def about(request):
    return render(request, 'about.html')

