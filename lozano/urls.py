
from django.contrib import admin
from django.urls import path, include

from lozano import views

urlpatterns = [
    # path( 'URL A LA CUAL APUNTO', BACKEND, name= Nombre de la variable)
    path('home/', views.lozanoHome, name='lozanoHome'),
    path('idiomas/', views.lozanoIdiomas, name='lozanoIdiomas'),
    path('404/', views.lozano404, name='lozano404'),
    path('idioma/<pk>', views.lozanoIdioma, name="lozanoIdioma"),
    path('pais/<pk>', views.lozanoPais, name="lozanoPais")
]