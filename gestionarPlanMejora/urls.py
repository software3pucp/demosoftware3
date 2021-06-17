from django.urls import path, include

from gestionarPlanMejora import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)
    path('listar/', views.listarPlanMejora, name="listarPlanMejora"),
    path('crearPlanMedicionAjax', views.crearAjax, name='crearPlanMejoraAjax'),
    path('crearPropuesta/<id_especialidad>', views.crearPropuesta, name="crearPropuesta"),
    path('editar/<pk>', views.editarPropuesta, name="editarPropuesta"),
    path('eliminar/', views.eliminarActividadxPropuesta, name="eliminarActividadxPropuesta"),
]