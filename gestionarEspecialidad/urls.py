from django.urls import path, include

from gestionarEspecialidad import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)
    path('listar/', views.listarEspecialidad, name="listarEspecialidad"),
    path('listar/<id_especialidad>', views.listarEspecialidadxCurso, name="listarEspecialidadxCurso"),
    # path('agregar/', views.agregarEspecialidad, name="agregarEspecialidad"),
    path('editar/<pk>', views.editarEspecialidad, name="editarEspecialidad"),

    path('agregar/<id_facultad>', views.agregarEspecialidad, name="agregarEspecialidad"),
    # path('editar', views.editarFacultad, name="editarFacultad"),
    # path('eliminar', views.eliminarFacultad, name="eliminarFacultad"),

]
