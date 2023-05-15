from django.urls import path, re_path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    re_path(r'^$', views.index, name="index"),
    re_path(r'^home/?$', views.home, name='home'),
    re_path(r'^courses/?$', views.courses, name='courses'),
    re_path(r'^signup/?$', views.signup, name='signup'),
    re_path(r'^login/?$', views.login, name='login'),
    re_path(r'^logout/?$', LogoutView.as_view(), name='logout'),
    re_path(r'^about/?$', views.about, name='about'),
    re_path(r'^contact/?$', views.contact, name='contact'),
    re_path(r'^course/<int:course_id>/?$',views.course, name='course'),
    re_path(r'^create_course/?$', views.create_course, name='create_course'),
    re_path(r'^login_wall/?$', views.login_wall, name='login_wall'),
    re_path(r'^temp_logout/?$', views.temp_logout, name='temp_logout')
]   
