from django.urls import path, include

from gestionarPlanMedicion import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)
    path('listar/', views.listarPlanMedicion, name="listarPlanMedicion"),
    path('crear/<pk>', views.crearPlanMedicion, name="crearPlanMedicion"),
    path('crearPlanMedicionAjax', views.crearAjax, name='crearPlanMedicionAjax'),
    path('historico/', views.historico, name='historico'),
    path('crearHistorico/<id_especialidad>', views.crearHistorico, name='crearHistorico'),
    path('listarHistorico/', views.listarHistorico, name='listarHistorico'),
    path('eliminarMedicion/', views.eliminarMedicion, name='eliminarMedicion')
]
