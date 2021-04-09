

from django.contrib import admin
from django.urls import path, include

from candidates2021 import views

urlpatterns = [
    # path( 'URL A LA CUAL APUNTO', BACKEND, name= Nombre de la variable)
    path('', views.ListCandidates, name='CdHome' ),
    # path('<pk>/', views., name='candidatos'),
    path('register/', views.Register, name='register'),
    path('delete/<pk>', views.Delete, name='delete'),
]

