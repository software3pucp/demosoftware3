from django.urls import path, include

from gestionarEspecialidad import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)
    path('listar/', views.listarEspecialidad, name="listarEspecialidad"),
<<<<<<< HEAD
    path('agregar/', views.agregarEspecialidad, name="agregarEspecialidad"),
    path('editar/<pk>', views.editarEspecialidad, name="editarEspecialidad"),
=======
    path('agregar/<id_facultad>', views.agregarEspecialidad, name="agregarEspecialidad"),
    # path('editar', views.editarFacultad, name="editarFacultad"),
>>>>>>> a0a27610132e3fdc3e93727bc2b66a926f230b16
    # path('eliminar', views.eliminarFacultad, name="eliminarFacultad"),
]
