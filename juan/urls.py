

from django.contrib import admin
from django.urls import path, include

from juan import views

urlpatterns = [
    # path( 'URL A LA CUAL APUNTO', BACKEND, name= Nombre de la variable)
    path('home/', views.juanHome, name='juanHome' ),
    path('listado/', views.listar, name='listado'),
]






