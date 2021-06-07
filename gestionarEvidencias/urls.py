from django.urls import path, include
from gestionarEvidencias import views

urlpatterns = [
    path('evidenciasxHorario/<id_curso>/<id_horario>', views.evidenciasxHorario, name='evidenciasxHorario'),
    path('editarEvidencia/', views.editarEvidenciaxHorario, name='editarEvidencia'),
    path('subirEvidencia/', views.subirEvidenciaxHorario, name='subirEvidenciaHorario'),
    path('eliminarEvidencia/', views.eliminarEvidenciaxHorario,name='eliminarEvidendia'),
    path('listarEvidencias/', views.listarEvidencias, name='listarEvidencias'),
]