
from django.contrib import admin
from django.urls import path
from app_booking import views

urlpatterns = [
    path('', views.index, name='index'),

    path('signup/', views.signup, name='signup'),

    path('register/', views.register, name='register'),  # Add this line for the register view

    path('login/', views.loginpage, name='login'), # patient login page

    path('drlogin/',views.drLogin, name='drlogin'),

    path('booking/', views.bookingPage, name='booking'),
    path('appointments/', views.appo_list, name='appointments'),  # New URL for appointments
]
