from django.urls import path, include

from gestionarNivel import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)
    path('/listar', views.listarNiv, name="listarNiv"),
    path('/editar/<pk>', views.editarNiv, name="editarNiv"),
    path('/crear', views.crearNiv, name="crearNiv")
]