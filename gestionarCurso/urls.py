from django.urls import path, include

from gestionarCurso import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)
    path('listar/', views.listarCurso, name="listarCurso"),
    path('listar/<id_curso>/', views.listarCursoxHorario, name="listarCursoxHorario"),
    path('editar/<id_curso>/', views.editarCurso, name="editarCurso"),
    path('eliminar/<id_curso>/', views.eliminarCurso, name="eliminarCurso"),
    path('agregar/<id_especialidad>/', views.agregarCurso, name="agregarCurso"),
]
