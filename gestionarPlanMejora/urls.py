from django.urls import path, include

from gestionarPlanMejora import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)
    path('editarActividad/', views.crearActividad, name="crearActividad"),
    path('editarActividad/', views.editarActividad, name="editarActividad"),
    path('subirEvidencia/', views.subirEvidencia, name="subirEvidencia"),
    path('editarEvidencia/', views.editarEvidencia, name="editarEvidencia"),

]