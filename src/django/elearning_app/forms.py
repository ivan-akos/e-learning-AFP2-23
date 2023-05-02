from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import django.contrib.auth as auth
from django.contrib import messages
from django.db import IntegrityError
from .models import Users
import hashlib
import pdb

@csrf_exempt
def register(request):
	if request.method == 'POST':
		neptun = request.POST['neptun']
		name = request.POST['name']
		password = request.POST['password']
		try:
			# Check field lengths
			if len(neptun) != 6:
				raise AssertionError('Neptun must be 6 characters long')
			if len(name) > 45:
				raise AssertionError('Name cannot be longer than 45 characters')
			# Hash the password
			hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
			# Create user
			user = Users.objects.create(neptun=neptun, name=name, password=hashed_password)
		except (AssertionError, IntegrityError) as e:
			messages.error(request, 'Registration error.')
			return
		#
		user.save()
		messages.success(request, 'Registration success.')


@csrf_exempt
def login(request):
	username = request.POST.get('neptun')
	password = request.POST.get('password')
	user = auth.authenticate(request, username=username, password=password)
	if user is not None:
		auth.login(request, user)
		messages.success(request, 'Sikeres bejelentkezés.')
	else:
		messages.error(request, 'Sikertelen bejelentkezés.')
		
