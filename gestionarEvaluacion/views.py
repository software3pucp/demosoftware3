from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

# Create your views here.

from gestionarEvaluacion.models import Alumno
from gestionarIndicadores.models import Indicador
from gestionarNivel.models import Nivel
def listarAlumno(request):
    listaAlumno = Alumno.objects.filter()
    listaIndicador = Indicador.objects.filter()
    context = {
        'listaAlumno': listaAlumno,
        'listaIndicador':listaIndicador
    }
    return render(request, 'gestionarEvaluacion/baseEvaluacion/base.html',context)


def agregarAlumno(request):
    nuevoAlumno = Alumno.objects.create(nombreAlumno=request.POST["nombreAlumno"],
                                        codigoAlumno=request.POST["codigoAlumno"])
    ser_instance = serializers.serialize('json', [nuevoAlumno,])
    return JsonResponse({"nuevoAlumno": ser_instance}, status=200)

def muestraRubrica(request):
    niveles = Nivel.objects.filter(state=request.POST["indicadorSeleccionado"])
    ser_instance = serializers.serialize('json', list(niveles),fields=('id','name','value','state'))
    return JsonResponse({"niveles": ser_instance}, status=200)