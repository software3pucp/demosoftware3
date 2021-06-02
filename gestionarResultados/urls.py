from django.urls import path, include

from gestionarResultados import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)
    path('crear/', views.crearResultado, name="crearResultado"),
    path('listar/', views.listarResultado, name="listarResultado"),
    path('editar/<pk>', views.editarResultado, name="editarResultado"),
]
