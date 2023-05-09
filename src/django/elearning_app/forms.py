from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import django.contrib.auth as auth
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.db import IntegrityError
import hashlib
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
			messages.success(request, 'Sikeres bejelentkezés.')
		else:
			messages.error(request, 'Sikertelen bejelentkezés.')
			
