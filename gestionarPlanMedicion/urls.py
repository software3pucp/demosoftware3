from django.urls import path, include

from gestionarPlanMedicion import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)
    path('listar/', views.listarPlanMedicion, name="listarPlanMedicion"),
    path('crear/<pk>', views.crearPlanMedicion, name="crearPlanMedicion"),
]