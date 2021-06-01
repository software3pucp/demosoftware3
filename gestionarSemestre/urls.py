from django.urls import path, include

from gestionarSemestre import views

urlpatterns = [
    path('agregar/', views.agregarSemestre, name='agregarSemestre'),
    path('listar/', views.listarSemestre, name="listarSemestre"),
    path('enviarCursoHorario/<pk>', views.enviarCursoHorario, name='enviarCursoHorario'),
]
