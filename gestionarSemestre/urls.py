from django.urls import path, include

from gestionarSemestre import views

urlpatterns = [
    path('/listar', views.listarSemestre, name="listarSemestre"),
]
