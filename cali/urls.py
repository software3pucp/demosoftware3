
from django.contrib import admin
from django.urls import path, include

from cali import views

urlpatterns = [
    # path( 'URL A LA CUAL APUNTO', BACKEND, name= Nombre de la variable)
    path('home/', views.caliHome, name='caliHome'),
    path('candidatos/<pk>', views.candidatoDetalle, name='candidatoDetalle'),
]






