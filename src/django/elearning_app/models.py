from django.db import models
from django.contrib.auth import get_user_model
import random
User = get_user_model()

class Courses(models.Model):
    code = models.CharField(unique=True, max_length=11)
    name = models.CharField(max_length=45)
    owner = models.ForeignKey(User, models.CASCADE, db_column='owner')

    class Meta:
        managed = True
        db_table = 'courses'

    def generate_code():
        r = 'EA' + ''.join(random.choices('0123456789', k=7))
        print(r)
        return r


class UsersCourses(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    course = models.ForeignKey(Courses, models.CASCADE, db_column='course')
    is_pending = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'users_courses'


class Lessons(models.Model):
    course = models.ForeignKey(Courses, models.CASCADE, db_column='course')
    name = models.CharField(max_length=45)
    nth = models.IntegerField()
    body = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lessons'


class Media(models.Model):
    owner = models.ForeignKey(User, models.CASCADE, db_column='owner')
    data = models.BinaryField()

    class Meta:
        managed = True
        db_table = 'media'
