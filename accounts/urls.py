from django.urls import path
from django.contrib import admin
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home),
    path('login/', views.sign_in, name = 'login'),
    path('register/', views.register, name = 'register'),
    path('picture_edit/', views.picture_edit),
]
