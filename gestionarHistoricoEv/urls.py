from django.urls import path, include

from gestionarHistoricoEv import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)
    path('listar/<pk>', views.listarHistorico, name="listarHistorico"),
]
