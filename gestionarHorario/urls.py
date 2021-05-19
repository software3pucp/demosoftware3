from django.urls import path, include

from gestionarHorario import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)
    path('listar/', views.listarHorario, name="listarHorario"),
    path('editar/<id_horario>/', views.editarHorario, name="editarHorario"),
    path('eliminar/<id_horario>/', views.eliminarHorario, name="eliminarHorario"),
    path('agregar/<id_curso>/', views.agregarHorario, name="agregarHorario"),
]
