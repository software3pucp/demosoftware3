from django.urls import path, include

from gestionarNiveles import views

urlpatterns = [
    path('niveles/', views.niveles, name="niveles"),
    path('crear/', views.crearNivel, name="crearNivel"),
    path('listarNiveles/', views.listarNiveles, name="listarNiveles"),
    path('editar/<pk>', views.editarNivel, name="editarNivel"),
    path('filtrarEspecialidades/', views.obtenerEspecialidades, name="filtrarEspecialidades"),
    path('eliminarNivel/', views.eliminarNivel, name="eliminarNivel"),
    path('editarNivel/',views.editarNivel,name='editarNivel'),
]
