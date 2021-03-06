from django.urls import path, include

from gestionarAsistentes import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)
    path('asistentes/', views.asistentes, name="asistentes"),
    path('registrar/', views.registrarAsistente, name="registrarAsistente"),
    path('listar/', views.listarAsistentes, name="listarAsistentes"),
    path('eliminar/', views.eliminarAsistente, name="eliminarAsistente"),
]
