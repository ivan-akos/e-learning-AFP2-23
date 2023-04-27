from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Courses


def index(request):
    return home(request)

def home(request):
    return render(request, 'home.html')

def courses(request):
    courses_list = Courses.objects.order_by("id")
    context = {"courses_list":courses_list}
    return render(request, 'courses.html',context)

def course(request,course_id):
    course = get_object_or_404(Courses,pk=course_id)
    return render(request, 'course.html',{"Course":course})



def signup(request):
    return render(request, 'signup.html') 

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')