from django.contrib import admin
from django.urls import path, include

from Jhonatan import views

urlpatterns = [
    path('home/', views.PolarHome, name='PolarHome')
]
