from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import django.contrib.auth as auth
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.db.models import Max
from django.db import IntegrityError
from django.shortcuts import redirect
import hashlib
import random
import string
import elearning_app.models as Models
import pdb

@csrf_exempt
def register(request):
	if request.method == 'POST':
		neptun = request.POST['neptun']
		email = request.POST['email']
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		password = make_password(request.POST['password'])
		try:
			# Check field lengths
			if len(neptun) != 6:
				raise AssertionError('Neptun must be 6 characters long')
			# Create user
		except (AssertionError, IntegrityError) as e:
			messages.error(request, 'Registration error.')
			return
		#
		user = User.objects.create(username=neptun,
									email=email,
									first_name=first_name,
									last_name=last_name,
									password=password
								)
		user.save()
		messages.success(request, 'Registration success.')


@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('neptun')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login successful.')
        else:
            messages.error(request, 'Login error.')
            
@csrf_exempt
def create_course(request):
    if request.method == 'POST':
        
        try:
            course = Models.Courses(
                    code = Models.Courses.generate_code(),
                    name = request.POST.get('name'),
                    owner = request.user
                )
            course.save()
            messages.success(request, 'New course created.')
        except:
            messages.error(request, 'Something is wrong.')
            
@csrf_exempt
def create_lesson(request, course):
        lesson = Models.Lessons(
                    course = course,
                    name = request.POST.get('name'),
                    nth = (course.lessons_set.aggregate(Max('nth'))['nth__max'] or 0)+1,
                    body = request.POST.get('body')
                )
        try:
            lesson.save()
            messages.success(request, 'New lesson created.')
        except:
            messages.error(request, 'Something is wrong.')

def process_course_form(request, course):
    operation = request.POST.get('operation')
    """ if operation == 'create':
        create_lesson(request, course)
        return """
    if operation == 'delete':
        model = request.POST.get('model')
        if model == 'course':
            course.delete()
            course.is_deleted = True
            return
        elif model == 'lesson':
            lesson = Models.Lessons.objects.get(pk=request.POST.get('to_delete'))
            lesson.delete()
            messages.success(request, 'Lesson deleted.')
        return
    if operation == 'update':
        model = request.POST.get('model')
        if model == 'course':
            course.name = request.POST.get('name')
            course.save()
        elif model == 'lesson':
            lesson = Models.Lessons.objects.get(pk=request.POST.get('to_update'))
            lesson.name = request.POST.get('name')
            lesson.body = request.POST.get('body')
            lesson.save()
        return
