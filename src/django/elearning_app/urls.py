from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('home/', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('signup', views.signup, name='signup'),
