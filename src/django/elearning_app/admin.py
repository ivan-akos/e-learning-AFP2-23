from django.contrib import admin

from .models import Courses
from .models import UsersCourses
from .models import Lessons
from .models import Media

admin.site.register(Courses)
admin.site.register(UsersCourses)
admin.site.register(Lessons)
admin.site.register(Media)
