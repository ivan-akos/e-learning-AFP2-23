from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.contrib import messages
import django.contrib.auth as auth
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import auth
from .models import *
from . import forms

def home(request):
    print(request.user)
    messages._queued_messages = []
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
    if hasattr(course, 'is_deleted'):
        return redirect('courses')
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
    return redirect('/')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def login_wall(request):
    return render(request, 'login_wall.html')
    
def list_users(request):   
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

def update_user(request, user_id):
    user = User.objects.get(id=user_id)
    if not request.user.is_authenticated:
        return render(request, 'login_wall.html')
    
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        messages.success(request, 'User updated successfully')
        return redirect('list_users')

    return render(request, 'update_user.html', {'user': user})


def user_delete(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User deleted successfully')
        return redirect('list_users')

    return render(request, 'user_delete.html', {'user': user})
