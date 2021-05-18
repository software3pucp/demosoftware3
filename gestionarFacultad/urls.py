from django.urls import path, include

from gestionarFacultad import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)
    path('listar/', views.listarFacultad, name="listarFacultad"),
    path('listar/<id_facultad>/', views.listarFacultadxEsp, name="listarFacultadxEsp"),

    path('editar/<id_facultad>/', views.editarFacultad, name="editarFacultad"),
    path('eliminar/<id_facultad>/', views.eliminarFacultad, name="eliminarFacultad"),

    path('crear/', views.agregarFacultad, name="agregarFacultad")
]
