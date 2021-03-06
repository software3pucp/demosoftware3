from django.urls import path, include

from gestionarResultadosMediciones import views

urlpatterns = [
    path('resultados/<pk>', views.resultadosMediciones, name="resultadosMediciones"),
    path('getListaProgresoCurso', views.getListaProgresoCurso, name="getListaProgresoCurso"),
    path('getPorcentajeMedia', views.getPorcentajeMedia, name="getPorcentajeMedia"),
    path('getPorcentajeTot', views.getPorcentajeTot, name="getPorcentajeTot"),
]