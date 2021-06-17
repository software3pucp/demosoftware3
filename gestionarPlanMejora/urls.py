from django.urls import path, include

from gestionarPlanMejora import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)

    #Plan de mejora
    path('planMejora/', views.planMejora, name="planMejora"),

    #propuestas
    path('crear/<id_especialidad>', views.crearPropuesta, name="crearPropuesta"),
    path('listarPropuestas/', views.listarPropuestas, name='listarPropuestas'),
    path('editar/<pk>', views.editarPropuesta, name="editarPropuesta"),
    path('eliminarPropuesta/', views.eliminarPropuesta, name="eliminarPropuesta"),
    path('filtrarEspecialidades/', views.filtrarEspecialidades, name="filtrarEspecialidades"),

    #actividades
    path('eliminarActividad/', views.eliminarActividadxPropuesta, name="eliminarActividadxPropuesta"),
    path('crearActividad/<id_propuesta>', views.crearActividad, name="crearActividad"),
    path('editarActividad/<pk>', views.editarActividad, name="editarActividad"),

    #evidencias
    path('subirEvidencia/<id_actividad>', views.subirEvidencia, name="subirEvidenciaActividad"),
    path('editarEvidencia/<pk>', views.editarEvidencia, name="editarEvidenciaActividad"),
    path('eliminarEvidencia/', views.eliminarEvidenciaxActividad, name="eliminarEvidenciaxActividad"),
]