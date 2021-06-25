from django.urls import path, include

from gestionarEvaluacion import views

urlpatterns = [
    path('evaluar/<pk>', views.evaluar, name='evaluar'),
    path('evaluarDocente/', views.evaluarDocente, name='evaluarDocente'),
    path('agregarAlumno/', views.agregarAlumno, name='agregarAlumno'),
    path('muestraRubrica/',views.muestraRubrica,name='muestraRubrica'),
    path('listarAlumno/',views.listarAlumno,name='listarAlumno'),
    path('guardarPuntuacion/',views.guardarPuntuacion,name='guardarPuntuacion'),
    path('eliminarAlumno/',views.eliminarAlumno,name='eliminarAlumno'),
    path('editarAlumno/',views.editarAlumno,name='editarAlumno'),
    path('importarAlumno',views.importarAlumno,name='importarAlumno'), #TODO::: FIX colocar "/" y refactorizar
    path('subirEvidencia/',views.subirEvidencia,name='subirEvidencia'),
    path('exportarMedicion/',views.exportarMedicion,name='exportarMedicion'),
    path('historial/',views.historial,name='historial'),
    path('listarCursoMedicion/',views.listarCursoMedicion,name='listarCursoMedicion'),
]
