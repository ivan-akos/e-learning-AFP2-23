from django.urls import path, re_path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
<<<<<<< HEAD
    re_path(r'^$', views.index, name="index"),
    re_path(r'^home/?$', views.home, name='home'),
    re_path(r'^courses/?$', views.courses, name='courses'),
    re_path(r'^signup/?$', views.signup, name='signup'),
    re_path(r'^login/?$', views.login, name='login'),
    re_path(r'^logout/?$', LogoutView.as_view(), name='logout'),
    re_path(r'^about/?$', views.about, name='about'),
    re_path(r'^contact/?$', views.contact, name='contact'),
=======
    path("", views.index, name="index"),
    path('home/', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
	path('logout/', views.logout, name='logout'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
>>>>>>> eabca9d9 (urls: +profile)
    path('course/<int:course_id>/',views.course, name='course'),
    re_path(r'^create_course/?$', views.create_course, name='create_course'),
    re_path(r'^login_wall/?$', views.login_wall, name='login_wall'),
    re_path(r'^temp_logout/?$', views.temp_logout, name='temp_logout')
]   
