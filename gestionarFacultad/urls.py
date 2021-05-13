from django.urls import path, include

from gestionarFacultad import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)
    path('listar/', views.listarFacultad, name="listarFacultad"),
    # path('editar', views.editarFacultad, name="editarFacultad"),
    # path('eliminar', views.eliminarFacultad, name="eliminarFacultad"),
    path('crear/',views.crearFacultad, name="crearFacultad")
]
