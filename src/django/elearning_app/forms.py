from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import django.contrib.auth as auth
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.db.models import Max
from django.db import IntegrityError
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
		whathaveidone = Models.Usere(username=neptun,
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
			messages.success(request, 'Sikeres bejelentkezés.')
		else:
			messages.error(request, 'Sikertelen bejelentkezés.')
			
@csrf_exempt
def create_course(request):
	if request.method == 'POST':
		course = Models.Courses(
				code = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(11)),
				name = request.POST.get('name'),
				owner = request.user
			)
		course.save()
		try:
#			course = Models.Courses(
#					code = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(11)),
#					name = request.POST.get('name'),
#					owner = request.user.id
#				)
			messages.success(request, 'Új kurzus létre hozva.')
		except:
			messages.error(request, 'Valami félrement.')
			
@csrf_exempt
def create_lesson(request, course):
		course = Models.Lessons(
					course = course,
					name = request.POST.get('name'),
					nth = (course.lessons_set.aggregate(Max('nth'))['nth__max'] or 0)+1,
					body = request.POST.get('body')
				)
		course.save()
		try:
			messages.success(request, 'Új óra létre hozva.')
		except:
			messages.error(request, 'Valami félrement.')

def process_course_form(request, course):
    switch = request.POST.get('delete')
    if switch == None:
        forms.create_lesson(request, course)
    elif switch == 'course':
        course.delete()
        return redirect('courses')
    elif switch == 'lesson':
        lesson = Models.Lessons.objects.get(pk=request.POST.get('to_delete'))
        lesson.delete()
        messages.success(request, 'Óra törölve.')
    else:
        pass
