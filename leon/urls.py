

from django.contrib import admin
from django.urls import path, include

from leon import views

urlpatterns = [
    # path( 'URL A LA CUAL APUNTO', BACKEND, name= Nombre de la variable)
    path('home/', views.leonHome, name='leonHome'),
    path('ajax/', views.ajax, name='urlAjax'),
    path('archivo/', views.leonArchivos, name='leonArchivos' ),
    path('idioma/<pk>', views.idiomaDetalle, name='idiomaDetalle'),
]












