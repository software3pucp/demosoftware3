from django.urls import path, include

from gestionarAcreditadoras import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)
    path('listar', views.listarAcreditadoras, name="listarAcreditadoras"),
    path('crear/<pk>', views.crearAcreditadoras, name="crearAcreditadoras"),
]