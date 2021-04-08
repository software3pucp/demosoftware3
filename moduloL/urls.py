

from django.contrib import admin
from django.urls import path, include

from raul import views

urlpatterns = [
    # path( 'URL A LA CUAL APUNTO', BACKEND, name= Nombre de la variable)
    path('home/', views.raulHome, name='raulHome' ),
    path('champion/<pk>', views.championDetalle, name='championDetalle'),
]

