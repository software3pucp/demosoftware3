from django.contrib import admin
from django.urls import path, include

from Jhonatan import views

urlpatterns = [
    path('home/', views.PolarHome, name='PolarHome'),
    path('UserList/', views.usuario_list, name='UserList'),
    path('editar/<pk>', views.editarOsitos, name='editarOsitos'),
    path('eliminar/<pk>', views.muerteOsito, name='muerteOsito'),
    path('detalle/<pk>', views.detalleOsitos, name='detalleOsitos'),
]
