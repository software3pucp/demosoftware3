from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.core import serializers
from gestionarCurso.models import Curso
from gestionarEspecialidad.models import Especialidad
from gestionarFacultad.models import Facultad


def listarCursos(request):

    if request.POST:
        print('***************************************************************************************************')
        print(request)
        print('***************************************************************************************************')
        if request.POST['operacion'] == 'listEspe':
            especialidades = Especialidad.objects.filter(facultad_id=request.POST['facultad'])
            data = serializers.serialize("json", especialidades)
            return JsonResponse({"resp": data}, status=200)
        elif request.POST['operacion'] == 'listCur':
            cursos = Curso.objects.filter(especialidad_id=request.POST['especialidad'])
            data = serializers.serialize("json", cursos)
            return JsonResponse({"resp": data}, status=200)
    facultades = Facultad.objects.filter()
    especialidades = Especialidad.objects.filter()
    estados = ["Activo","Inactivo"]
    context = {
        'facultades' : facultades,
        'especialidades' : especialidades,
        'estados' : estados,
    }
    return render(request,'gestionarPlanMedicion/listarCursos.html',context)

def editarCursos(request):
    context = {

    }
    return render(request,'gestionarPlanMedicion/editarCursos.html',context)

