from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
from demosoftware3.settings import MEDIA_URL
from gestionarEvaluacion.models import Alumno
from gestionarHorario.models import Horario
from gestionarIndicadores.models import Indicador
from gestionarRubrica.models import Rubrica
from gestionarNivel.models import Nivel
from gestionarCurso.models import Curso
def evaluar(request,pk):
    media_path = MEDIA_URL
    listaAlumno = reversed(Alumno.objects.filter(estado=1)) #Lista de horarios
    listaIndicador = Indicador.objects.filter(estado=1)
    cursoSeleccionado = Curso.objects.get(pk=pk)
    horario= Horario.objects.get(pk=1) # por ahora se trabaja con un horario, estan harcodeados
    listaHorario= Horario.objects.filter(curso_id=pk); #listaDeHorario asociado a un curso
    context = {
        'media_path': media_path,
        'listaAlumno': listaAlumno,
        'listaIndicador': listaIndicador,
        'horario':horario,
        'cursoSeleccionado':cursoSeleccionado,
        'listaHorario':listaHorario,
    }
    return render(request, 'gestionarEvaluacion/baseEvaluacion/base.html',context)

def agregarAlumno(request):
    niveles = Nivel.objects.filter(state=1)
    nuevoAlumno = Alumno.objects.create(nombreAlumno=request.POST["nombreAlumno"],
                                        codigoAlumno=request.POST["codigoAlumno"],
                                        horario_id=request.POST["horario"])
    ser_instance = serializers.serialize('json', [nuevoAlumno,])
    ser_instance2 = serializers.serialize('json', list(niveles), fields=('id', 'name', 'value', 'state'))
    return JsonResponse({"nuevoAlumno": ser_instance,"niveles": ser_instance2 }, status=200)

def guardarPuntuacion(request):
    alumno = Alumno.objects.get(pk=request.POST["idAlumno"])
    descripcion = Rubrica.objects.get(indicador_id=request.POST["indicadorSeleccionado"],nivel_id=request.POST["nivelSeleccionado"]).descripcion
    alumno.descripcionP = descripcion
    alumno.valorNota = Nivel.objects.get(pk =request.POST["nivelSeleccionado"]).value
    alumno.rubrica_id = Rubrica.objects.get(indicador_id=request.POST["indicadorSeleccionado"],nivel_id=request.POST["nivelSeleccionado"]).pk
    alumno.calificado = 1
    alumno.save()
    return JsonResponse({},status=200)

def editarAlumno(request):
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
    niveles = Nivel.objects.filter(state=1)
    rubrica = Rubrica.objects.filter(indicador_id=request.POST["indicadorSeleccionado"])
    indicador = Indicador.objects.get(pk=request.POST["indicadorSeleccionado"])
    ser_instance = serializers.serialize('json', list(rubrica),fields=('id','descripcion','especialidad','indicador','nivel'))
    ser_instance2 = serializers.serialize('json',[indicador,])
    ser_instance3 = serializers.serialize('json', list(niveles),fields=('id','name','value','state'))
    return JsonResponse({"rubrica": ser_instance,"indicador":ser_instance2, "niveles": ser_instance3 }, status=200)

def listarAlumno(request):
    filtrado = request.POST["filtrado"]
    niveles = Nivel.objects.filter(state=1)
    if (filtrado!=""):
        if (filtrado.isnumeric()):
            listaAlumno = reversed(Alumno.objects.filter(codigoAlumno=filtrado, horario_id = request.POST["horarioSeleccionado"],estado=1))
        else:
            listaAlumno = reversed(Alumno.objects.filter(nombreAlumno__contains=filtrado,horario_id=request.POST["horarioSeleccionado"],estado=1))
    else:
        listaAlumno = reversed(Alumno.objects.filter(horario_id=request.POST["horarioSeleccionado"],estado=1))

    ser_instance = serializers.serialize('json', list(listaAlumno),fields=('id', 'nombreAlumno', 'codigoAlumno', 'horario','calificado', 'valorNota'))
    ser_instance2 = serializers.serialize('json', list(niveles), fields=('id', 'name', 'value', 'state'))
    return JsonResponse({"listaAlumno": ser_instance, "niveles": ser_instance2},  status=200)