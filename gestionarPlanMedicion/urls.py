from django.urls import path, include

from gestionarPlanMedicion import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)
    path('listar', views.listarCursos, name="listarCursos"),
    path('editar/<pk>', views.editarCursos, name="editarCursos"),
]