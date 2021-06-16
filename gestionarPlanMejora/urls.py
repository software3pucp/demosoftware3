from django.urls import path, include

from gestionarPlanMejora import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)
    path('listar/', views.listarPlanMejora, name="listarPlanMejora"),
    path('crear/<pk>', views.crearPlanMejora, name="crearPlanMejora"),
    path('crearPlanMedicionAjax', views.crearAjax, name='crearPlanMejoraAjax'),
    path('editar/<pk>', views.editarPropuesta, name="editarPropuesta"),
]