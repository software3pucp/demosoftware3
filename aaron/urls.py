from django.contrib import admin
from django.urls import path, include

from aaron import views

urlpatterns = [
    # path( 'URL A LA CUAL APUNTO', BACKEND, name= Nombre de la variable)
    path('home/', views.aaronHome, name='aaronHome'),
    path('listaWaffles/', views.listaWaffles, name='listaWaffles'),
    path('detalle/<pk>', views.detalleWaffles, name='detalleWaffles'),
    path('editar/<pk>', views.editarWaffles, name='editarWaffles'),
    path('eliminar/<pk>', views.eliminarWaffles, name='eliminarWaffles')
]
