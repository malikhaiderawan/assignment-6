from django.contrib import admin
from django.urls import path
from formapp import views



urlpatterns = [


    path('register/', views.register, name='register'),
    path('create_post/', views.create_post, name='create_post'),
]
