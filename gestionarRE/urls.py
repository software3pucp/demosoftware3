from django.urls import path, include

from gestionarRE import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)
    path('listar', views.listarRE, name="listarRE"),
    path('editar/<pk>', views.editarRE, name="editarRE"),
]