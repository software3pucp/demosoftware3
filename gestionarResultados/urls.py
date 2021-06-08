from django.urls import path, include

from gestionarResultados import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)
    path('crear/<id_especialidad>', views.crearResultado, name="crearResultado"),
    path('resultados/', views.Resultados, name="resultados"),
    path('editar/<pk>', views.editarResultado, name="editarResultado"),
    path('obtenerEspecialidades/', views.obtenerEspecialidades, name="obtenerEspecialidades"),
]
