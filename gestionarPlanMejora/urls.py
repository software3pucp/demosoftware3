from django.urls import path, include

from gestionarPlanMejora import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)
    path('listar/', views.listarPlanMejora, name="listarPlanMejora"),
    path('crearPlanMedicionAjax', views.crearAjax, name='crearPlanMejoraAjax'),
    path('crearPropuesta/<id_especialidad>', views.crearPropuesta, name="crearPropuesta"),
    path('editar/<pk>', views.editarPropuesta, name="editarPropuesta"),
    path('eliminar/', views.eliminarActividadxPropuesta, name="eliminarActividadxPropuesta"),
    path('crearActividad/', views.crearActividad, name="crearActividad"),
    path('editarActividad/<pk>', views.editarActividad, name="editarActividad"),
    path('subirEvidencia/<id_actividad>', views.subirEvidencia, name="subirEvidenciaActividad"),
    path('editarEvidencia/<pk>', views.editarEvidencia, name="editarEvidenciaActividad"),
    path('eliminarEvidencia/', views.eliminarEvidenciaxActividad, name="eliminarEvidenciaxActividad"),
]