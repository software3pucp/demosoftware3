#ESTOS SON LOS URLS DEL MÓDULO
from django.contrib import admin
from django.urls import path

from authentication import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)
    #path('login/', views.RenderLogin.as_view(), name="login"),
    #path('add/', views.RenderLogin, name='user'),
    #path('',views.Show, name='showUsers')

]
