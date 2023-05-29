from django.urls import path, re_path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    re_path(r'^$', views.home, name="index"),
    re_path(r'^home/?$', views.home, name='home'),
    re_path(r'^courses/?$', views.courses, name='courses'),
    re_path(r'^signup/?$', views.signup, name='signup'),
    re_path(r'^login/?$', views.login, name='login'),
    path("profile/<int:user_id>/", views.profile, name="profile"),
    re_path(r'^logout/?$', views.logout, name='logout'),
    re_path(r'^about/?$', views.about, name='about'),
    re_path(r'^contact/?$', views.contact, name='contact'),
    path('course/<int:course_id>/',views.course, name='course'),
    path("update_course/<int:course_id>/", views.update_course, name="update_course"),
    re_path(r'^login_wall/?$', views.login_wall, name='login_wall'),
]   
