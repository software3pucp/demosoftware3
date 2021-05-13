from django.urls import path, include

from gestionarEspecialidad import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)
    path('listar/', views.listarEspecialidad, name="listarEspecialidad"),
    path('agregar/<id_facultad>', views.agregarEspecialidad, name="agregarEspecialidad"),
    # path('editar', views.editarFacultad, name="editarFacultad"),
    # path('eliminar', views.eliminarFacultad, name="eliminarFacultad"),
]
