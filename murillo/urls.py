from django.contrib import admin
from django.urls import path, include
from murillo import views

urlpatterns = [
    # path( 'URL A LA CUAL APUNTO', BACKEND, name= Nombre de la variable)
    path('home/', views.murilloHome, name='murilloHome')
]