from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

# Create your views here.

from gestionarEvaluacion.models import Alumno

def listarAlumno(request):
    listaAlumno = Alumno.objects.filter()
    context = {
        'listaAlumno': listaAlumno
    }
    return render(request, 'gestionarEvaluacion/baseEvaluacion/base.html',context)


def agregarAlumno(request):
    nuevoAlumno = Alumno.objects.create(nombreAlumno=request.POST["nombreAlumno"],
                                        codigoAlumno=request.POST["codigoAlumno"])
    ser_instance = serializers.serialize('json', [nuevoAlumno,])
    return JsonResponse({"nuevoAlumno": ser_instance}, status=200)