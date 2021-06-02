from django.urls import path, include

from gestionarAcreditadoras import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)
    path('listar', views.listarAcreditadoras, name="listarAcreditadoras"),
    path('editar/<pk>', views.editarAcreditadoras, name="editarAcreditadoras"),
]