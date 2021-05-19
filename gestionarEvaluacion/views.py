from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

# Create your views here.

from gestionarEvaluacion.models import Alumno
from gestionarIndicadores.models import Indicador
from gestionarRubrica.models import Rubrica
from gestionarNivel.models import Nivel
def evaluar(request):
    listaAlumno = reversed(Alumno.objects.filter(estado=1)) #Lista de horarios
    listaIndicador = Indicador.objects.filter()
    context = {
        'listaAlumno': listaAlumno,
        'listaIndicador':listaIndicador
    }
    return render(request, 'gestionarEvaluacion/baseEvaluacion/base.html',context)


def agregarAlumno(request):
    niveles = Nivel.objects.all()
    nuevoAlumno = Alumno.objects.create(nombreAlumno=request.POST["nombreAlumno"],
                                        codigoAlumno=request.POST["codigoAlumno"],
                                        horario=request.POST["horario"])
    ser_instance = serializers.serialize('json', [nuevoAlumno,])
    ser_instance2 = serializers.serialize('json', list(niveles), fields=('id', 'name', 'value', 'state'))
    return JsonResponse({"nuevoAlumno": ser_instance,"niveles": ser_instance2 }, status=200)

def guardarPuntuacion(request):
    alumno = Alumno.objects.get(pk=request.POST["idAlumno"])
    descripcion = Rubrica.objects.get(indicador_id=request.POST["indicadorSeleccionado"],nivel_id=request.POST["nivelSeleccionado"]).descripcion
    alumno.descripcionP = descripcion
    alumno.save()
    return JsonResponse({},status=200)

def editarAlumno(request):
    print("toy aqui jeje")
    print(request)
    print("############################")
    alumno = Alumno.objects.get(pk = request.POST["idAlumno"])
    nuevoCodigo = request.POST["codigoAlumno"]
    nuevoNombre = request.POST["nombreAlumno"]
    alumno.codigoAlumno = nuevoCodigo
    alumno.nombreAlumno = nuevoNombre
    alumno.save()
    return JsonResponse({}, status=200)

def eliminarAlumno(request):
    alumno = Alumno.objects.get(pk = request.POST["idAlumno"])
    alumno.estado = 0
    alumno.save()
    return JsonResponse({}, status=200)

def muestraRubrica(request):
    niveles = Nivel.objects.all()
    rubrica = Rubrica.objects.filter(indicador_id=request.POST["indicadorSeleccionado"])
    indicador = Indicador.objects.get(pk=request.POST["indicadorSeleccionado"])
    ser_instance = serializers.serialize('json', list(rubrica),fields=('id','descripcion','especialidad','indicador','nivel'))
    ser_instance2 = serializers.serialize('json',[indicador,])
    ser_instance3 = serializers.serialize('json', list(niveles),fields=('id','name','value','state'))
    return JsonResponse({"rubrica": ser_instance,"indicador":ser_instance2, "niveles": ser_instance3 }, status=200)

def listarAlumno(request):
    filtrado = request.POST["filtrado"]
    niveles = Nivel.objects.all()
    if (filtrado!=""):
        if (filtrado.isnumeric()):
            listaAlumno = reversed(Alumno.objects.filter(codigoAlumno=filtrado, horario=request.POST["horarioSeleccionado"],estado=1))
        else:
            listaAlumno = reversed(Alumno.objects.filter(nombreAlumno=filtrado,horario=request.POST["horarioSeleccionado"],estado=1))
    else:
        listaAlumno = reversed(Alumno.objects.filter(horario=request.POST["horarioSeleccionado"],estado=1))
    ser_instance = serializers.serialize('json', list(listaAlumno),fields=('id', 'nombreAlumno', 'codigoAlumno', 'horario'))
    ser_instance2 = serializers.serialize('json', list(niveles), fields=('id', 'name', 'value', 'state'))
    return JsonResponse({"listaAlumno": ser_instance, "niveles": ser_instance2},  status=200)