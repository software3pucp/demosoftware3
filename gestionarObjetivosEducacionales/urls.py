from django.urls import path, include

from gestionarObjetivosEducacionales import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)
    #Objetivos educacionales
    path('objetivos/', views.objetivos, name="objetivos"),
    path('listar/', views.listarObjetivos, name="listarObjetivos"),
    path('crear/', views.crearObjetivo, name="crearObjetivo"),
    path('editar/', views.editarObjetivo, name="editarObjetivo"),
    path('eliminar/', views.eliminarObjetivo, name="eliminarObjetivo"),
    path('obtEspecialidades/', views.obtEspecialidades, name="obtEspecialidades"),
]
