from django.http import JsonResponse
from django.shortcuts import render
from gestionarCurso.models import Curso

# Create your views here.
from gestionarEspecialidad.models import Especialidad
from gestionarFacultad.models import Facultad


def listarCursos(request):

    if request.POST:
        print('*******************************************************************************************************')
        print(request.POST)
        print('*******************************************************************************************************')
        return JsonResponse({"response": 'Correct'}, status=200)

    estados = ["Activo","Inactivo"]
    cursos = Curso.objects.filter()
    context = {
        'estados' : estados,
        'cursos' : cursos
    }
    return render(request,'gestionarPlanMedicion/listarCursos.html',context)

def editarCursos(request):
    context = {

    }
    return render(request,'gestionarPlanMedicion/editarCursos.html',context)

