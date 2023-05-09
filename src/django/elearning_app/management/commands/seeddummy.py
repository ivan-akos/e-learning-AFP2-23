from django.core.management.base import BaseCommand
from django_seed import Seed
from elearning_app.models import *
from django.contrib.auth.models import User
import subprocess
import string
import hashlib
import random
import os

class Command(BaseCommand):
	help = 'Seed dummy data.'

	media_dir = subprocess.check_output(['git', '-C', '.', 'rev-parse', '--show-toplevel']).decode("utf-8")[:-1]  + '/src/db/dummy_media/'
	media = os.listdir(media_dir)
	media_index = 0
	def get_media(self, x):
		swp = self.media_index
		self.media_index += 1
		with open(self.media_dir + self.media[swp], 'rb') as f:
			return f.read()

	def handle(self, *args, **options):
		seeder = Seed.seeder()

		seeder.add_entity(User, 20, {
			'is_staff': False,
			'is_superuser': False,
		})
		#
		seeder.add_entity(Courses, 10, {
			'owner': lambda x: seeder.faker.random_element(User.objects.all()),
			'code': lambda x: 'EA' + ''.join(random.choices('0123456789', k=7))
		})
		#
		seeder.add_entity(UsersCourses, 10, {
			'user': lambda x: seeder.faker.random_element(User.objects.all()),
			'course': lambda x: seeder.faker.random_element(Courses.objects.all())
		})
		#
		seeder.add_entity(Lessons, 10)
		#
		seeder.add_entity(Media, len(self.media), {
			'data': self.get_media
		})


		inserted_pks = seeder.execute()
