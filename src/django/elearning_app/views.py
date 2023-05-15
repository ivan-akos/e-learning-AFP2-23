from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.contrib import messages
from django.shortcuts import redirect
from .models import *
from . import forms

def temp_logout(request):
    return render(request, 'temp_logout.html')

def index(request):
    return home(request)

def home(request):
    messages._queued_messages = []
    forms.login(request)
    return render(request, 'home.html')

def courses(request):
    courses_list = Courses.objects.order_by("id")
    context = {"courses_list":courses_list}
    return render(request, 'courses.html',context)

def course(request, course_id):
    course = get_object_or_404(Courses, pk=course_id)
    if request.method == 'POST':
        switch = request.POST.get('delete')
        if switch == None:
            forms.create_lesson(request, course)
        elif switch == 'course':
            course.delete()
            return redirect('courses')
        elif switch == 'lesson':
            lesson = Lessons.objects.get(pk=request.POST.get('to_delete'))
            lesson.delete()
            messages.success(request, 'Óra törölve.')
        else:
            pass
    return render(request, 'course.html', {"Course":course})



def signup(request):
    messages._queued_messages = []
    forms.register(request)
    return render(request, 'signup.html') 

def login(request):
    messages._queued_messages = []
    forms.login(request)
    return render(request, 'login.html') 

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def create_course(request):
    if not request.user.is_authenticated:
        return render(request, 'login_wall.html')
    forms.create_course(request)
    return render(request, 'create_course.html')

def login_wall(request):
    return render(request, 'login_wall.html')
