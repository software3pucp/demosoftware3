from django.contrib import admin
from django.urls import path, include

from lozano import views

urlpatterns = [
    # path( 'URL A LA CUAL APUNTO', BACKEND, name= Nombre de la variable)
    path('home/',views.lozanoHome, name='lozanoHome'),
    path('pokemon/insertar',views.lozanoInsertarPokemon,name='lozanoInsertarPokemon'),
    path('pokemon/editar/<pk>',views.lozanoEditarPokemon,name='lozanoEditarPokemon'),
    path('pokemon/<pk>',views.lozanoPokemonDetalle,name='lozanoPokemonDetalle'),
]