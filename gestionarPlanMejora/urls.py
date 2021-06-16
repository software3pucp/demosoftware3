from django.urls import path, include

from gestionarPlanMejora import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)
    path('crearActividad/', views.crearActividad, name="crearActividad"),
    path('editarActividad/<pk>', views.editarActividad, name="editarActividad"),
    path('subirEvidencia/<id_actividad>', views.subirEvidencia, name="subirEvidenciaActividad"),
    path('editarEvidencia/<pk>', views.editarEvidencia, name="editarEvidenciaActividad"),
    path('eliminarEvidencia/', views.eliminarEvidenciaxActividad, name="eliminarEvidenciaxActividad"),
]