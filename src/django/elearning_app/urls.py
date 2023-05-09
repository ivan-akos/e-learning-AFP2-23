from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", views.index, name="index"),
    path('home/', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('course/<int:course_id>/',views.course, name='course'),
    path('create_course', views.create_course, name='create_course'),
    path('login_wall', views.login_wall, name='login_wall'),
    path('temp_logout', views.temp_logout, name='temp_logout')
]   
