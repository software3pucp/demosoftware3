from django.urls import path, include

from gestionarNiveles import views

urlpatterns = [
    path('niveles/', views.niveles, name="niveles"),
    path('crear/', views.crearNivel, name="crearNivel"),
    path('editar/<pk>', views.editarNiv, name="editarNivel"),
    path('filtrarEspecialidades/', views.obtenerEspecialidades, name="filtrarEspecialidades"),
]
