from django.urls import path, include

from gestionarEvidencias import views

urlpatterns = [
    path('listarEvidenciasHorario/<id_horario>', views.listarEvidenciaHorario, name='listarEvidenciasHorario'),
    path('editar/<pk>', views.editarEvidencia, name='editarEvidencia'),
    path('subir/', views.subirEvidenciaHorario, name="subirEvidenciaHorario"),
]