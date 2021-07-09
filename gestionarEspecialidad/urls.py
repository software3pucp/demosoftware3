from django.urls import path, include

from gestionarEspecialidad import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)
    path('listar/', views.listarEspecialidad, name="listarEspecialidad"),
    path('listarEspecialidadDirector/', views.listarEspecialidadDirector, name="listarEspecialidadDirector"),
    path('listar/<id_especialidad>/', views.listarEspecialidadxCurso, name="listarEspecialidadxCurso"),
    path('editar/<id_especialidad>/', views.editarEspecialidad, name="editarEspecialidad"),
    path('eliminar/<id_especialidad>/', views.eliminarEspecialidad, name="eliminarEspecialidad"),
    path('desactivar/<id_especialidad>/', views.eliminarEspecialidad2, name="eliminarEspecialidad2"),
    path('agregar/<id_facultad>/', views.agregarEspecialidad, name="agregarEspecialidad"),
]
