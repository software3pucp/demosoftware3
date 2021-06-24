from django.urls import path, include

from gestionarResultados import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)

    # Plan de resultados
    path('planDeResultado/', views.planDeResultado, name="planDeResultado"),
    path('crearPlanResultado/<id_especialidad>', views.crearPlanResultado, name="crearPlanResultado"),
    path('listarPlanResultado/', views.listarPlanResultado, name="listarPlanResultado"),
    path('editarPlanDeResultado/<pk>', views.editarPlanDeResultado, name="editarPlanDeResultado"),
    path('eliminarPlanResultado/', views.eliminarPlanResultado, name="eliminarPlanResultado"),
    path('activarPlan/', views.activarPlan, name="activarPlan"),
    path('desactivarPlan/', views.desactivarPlan, name="desactivarPlan"),
    path('obtenerEspecialidades/', views.obtenerEspecialidades, name="obtenerEspecialidades"),

    # Resultados
    path('crear/<id_plan>', views.crearResultado, name="crearResultado"),
    path('resultados/<id_plan>', views.Resultados, name="resultados"),
    path('listarResultados/', views.listarResultados, name='listarResultados'),
    path('editar/<pk>', views.editarResultado, name="editarResultado"),
    path('eliminar/', views.eliminarResultado, name="eliminarResultado"),
]
