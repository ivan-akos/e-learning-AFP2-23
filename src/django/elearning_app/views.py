from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib import auth
from .models import *
from . import forms
from django.contrib import auth

def temp_logout(request):
    return render(request, 'temp_logout.html')

def index(request):
    return home(request)

def home(request):
    forms.login(request)
    if request.user.is_authenticated:
        users_courses = UsersCourses.objects.filter(user_id=int(request.user.id))
    else:
        users_courses = []
    
    return render(request, 'home.html', {"users_courses":users_courses})

def courses(request):
    if not request.user.is_authenticated:
        return render(request, 'login_wall.html')
    forms.create_course(request)
    courses_list = Courses.objects.order_by("id")
    return render(request, 'courses.html', {"courses_list":courses_list})

def profile(request, user_id):
    user = User.objects.get(pk=int(user_id))
    owned_courses = Courses.objects.filter(owner=int(user_id))
    users_courses = UsersCourses.objects.filter(user_id=int(user_id))
    
    return render(request, 'profile.html', {"user":user,
                                            "owned_courses":owned_courses,
                                            "users_courses":users_courses})

def course(request, course_id):
    course = get_object_or_404(Courses, pk=course_id)
    forms.create_lesson(request, course)
    return render(request, 'course.html', {"Course":course})

def update_course(request, course_id):
    course = get_object_or_404(Courses, pk=course_id)
    if request.method == 'POST':
        forms.process_course_form(request, course)
    return render(request, 'update_course.html', {"Course":course})

def signup(request):
    messages._queued_messages = []
    forms.register(request)
    return render(request, 'signup.html') 

def login(request):
    messages._queued_messages = []
    forms.login(request)
    return render(request, 'home.html') 

def logout(request):
    auth.logout(request)
    return home(request)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def create_course(request):
    
    return render(request, 'create_course.html')

def login_wall(request):
    return render(request, 'login_wall.html')
