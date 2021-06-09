from django.urls import path, include

from gestionarResultados import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)
    path('crear/<id_especialidad>', views.crearResultado, name="crearResultado"),
    path('resultados/', views.Resultados, name="resultados"),
    path('listarResultados/', views.listarResultados, name='listarResultados'),
    path('editar/<pk>', views.editarResultado, name="editarResultado"),
    path('eliminar/', views.eliminarResultado, name="eliminarResultado"),
    path('obtenerEspecialidades/', views.obtenerEspecialidades, name="obtenerEspecialidades"),
]
