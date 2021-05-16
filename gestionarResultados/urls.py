from django.urls import path, include

from gestionarResultados import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)
    path('listar/', views.listarResultado, name="listarResultado"),
    path('crear/', views.crearResultado, name="crearResultado"),
    path('editar/<pk>/', views.editarResultado, name="editarResultado"),
    #path('listar/<id_Resultado>/', views.listarIndicadoresxResultado, name="listarIndicadoresxResultado"),
]