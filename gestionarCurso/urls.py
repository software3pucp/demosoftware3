from django.urls import path, include

from gestionarCurso import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)
    path('listar/', views.listarCurso, name="listarCurso"),
    # path('agregar/', views.agregarEspecialidad, name="agregarEspecialidad"),
    path('editar/<pk>', views.editarCurso, name="editarCurso"),

    path('agregar/<id_especialidad>', views.agregarCurso, name="agregarCurso"),
    # path('editar', views.editarFacultad, name="editarFacultad"),
    # path('eliminar', views.eliminarFacultad, name="eliminarFacultad"),

]
