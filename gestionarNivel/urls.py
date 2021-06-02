from django.urls import path, include

from gestionarNivel import views

urlpatterns = [
    path('agregar/', views.agregarNivel, name="agregarNivel"),
    path('listar/', views.listarNivel, name="listarNivel"),
    path('editar/<pk>', views.editarNiv, name="editarNiv"),
]