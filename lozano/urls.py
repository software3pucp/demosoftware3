
from django.contrib import admin
from django.urls import path, include

from lozano import views

urlpatterns = [
    # path( 'URL A LA CUAL APUNTO', BACKEND, name= Nombre de la variable)
    path('home/', views.lozanoHome, name='lozanoHome' ),
    path('404/', views.lozano404, name='lozano404')
]