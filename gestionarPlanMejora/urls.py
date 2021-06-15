from django.urls import path, include

from gestionarPlanMedicion import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)
    path('editarActividad/', views.listarPlanMedicion, name="listarPlanMedicion"),

]