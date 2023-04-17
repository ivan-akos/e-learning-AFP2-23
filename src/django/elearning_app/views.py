from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return home(request)

def home(request):
    return render(request, 'home.html')    