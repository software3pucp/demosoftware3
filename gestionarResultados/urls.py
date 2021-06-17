from django.urls import path, include

from gestionarResultados import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)
    path('crear/<id_especialidad>/<id_plan>', views.crearResultado, name="crearResultado"),
    path('resultados/<pk_plan>', views.Resultados, name="resultados"),
    path('listarResultados/', views.listarResultados, name='listarResultados'),
    path('editar/<pk>/<id_plan>', views.editarResultado, name="editarResultado"),
    path('eliminar/', views.eliminarResultado, name="eliminarResultado"),
    path('obtenerEspecialidades/', views.obtenerEspecialidades, name="obtenerEspecialidades"),
    path('planDeResultado/', views.planDeResultado, name="planDeResultado"),
    path('crearPlanResultado/<id_especialidad>', views.crearPlanResultado, name="crearPlanResultado"),
    path('listarPlanResultado/', views.listarPlanResultado, name="listarPlanResultado"),
    path('activarPlan/', views.activarPlan, name="activarPlan"),
    path('desactivarPlan/', views.desactivarPlan, name="desactivarPlan"),
]
