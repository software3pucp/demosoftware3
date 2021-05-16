from django.shortcuts import render
from gestionarCurso.models import Curso

# Create your views here.

def listarCursos(request):
    facultad = "Ingenieria Informática"
    estados = ["Activo","Inactivo"]
    cursos = Curso.objects.filter(especialidad=1)
    context = {
        'facultad' : facultad,
        'estados' : estados,
        'cursos' : cursos
    }
    return render(request,'gestionarPlanMedicion/listarCursos.html',context)

def editarCursos(request):
    context = {

    }
    return render(request,'gestionarPlanMedicion/editarCursos.html',context)

