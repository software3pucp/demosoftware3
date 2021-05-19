from django.urls import path, include

from gestionarEvaluacion import views

urlpatterns = [
    path('evaluar/', views.evaluar, name='evaluar'),
    path('agregarAlumno/', views.agregarAlumno, name='agregarAlumno'),
    path('muestraRubrica/',views.muestraRubrica,name='muestraRubrica'),
    path('listarAlumno/',views.listarAlumno,name='listarAlumno'),
    path('guardarPuntuacion/',views.guardarPuntuacion,name='guardarPuntuacion'),
    path('eliminarAlumno/',views.eliminarAlumno,name='eliminarAlumno'),

]
