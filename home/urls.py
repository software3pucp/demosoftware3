#ESTOS SON LOS URLS DEL MÓDULO
from django.contrib import admin
from django.urls import path, include

from home import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)
    path('', views.RenderHome.as_view(), name="home"),
    path('home_base',views.base, name="base")
]
