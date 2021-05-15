from django.urls import path, include

from gestionarEvaluacion import views

urlpatterns = [
    path('listarAlumno/', views.listarAlumno, name='listarAlumno'),
    path('agregarAlumno/', views.agregarAlumno, name='agregarAlumno'),
]
