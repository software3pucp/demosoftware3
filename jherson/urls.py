from django.contrib import admin
from django.urls import path, include
from jherson import views

urlpatterns=[

    path('home/', views.jhersonHome, name= 'jhersonHome'),
    path('pokemon/insertar', views.jhersonInsertarPokemon, name='jhersonInsertarPokemon')
]
