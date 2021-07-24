from django.urls import path, include

from gestionarIndicadores import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)
    path('agregar/<id_resultado>/', views.agregarIndicador, name="agregarIndicador"),
    path('editar/<pk>/', views.editarIndicador,name="editarIndicador"),
    path('ver/<pk>/', views.verIndicador,name="verIndicador"),
    path('eliminar/', views.eliminarIndicadorxResultado, name="eliminarIndicadorxResultado"),
    path('agregarDescripcion/', views.agregarDescipcionNivel, name="agregarDescipcionNivel"),
]