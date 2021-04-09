

from django.contrib import admin
from django.urls import path, include

from Candidatos import views

urlpatterns = [
    # path( 'URL A LA CUAL APUNTO', BACKEND, name= Nombre de la variable)
    path('', views.ListCandidates, name='CdHome' ),
    # path('<pk>/', views., name='candidatos'),
    # path('register/', views., name='register'),
]

