from django.contrib import admin
from django.urls import path, include

from ale import views

urlpatterns = [
    # path( 'URL A LA CUAL APUNTO', BACKEND, name= Nombre de la variable)
    path('home/', views.aleHome, name='aleHome' ),
    path('lista/',views.usuario_list, name='aleList'),
    path('eliminar/<pk>', views.eliminarPersonajes, name='eliminarPersonajes'),
    path('editar/<pk>', views.editarPersonajes, name='editarPersonajes')
]
