from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.staticfiles import finders
from django.contrib.auth.decorators import login_required
# Create your views here.
from demosoftware3.settings import MEDIA_URL
from gestionarCurso.models import Curso
from gestionarEvidencias.models import EvidenciasxHorario
from gestionarHorario.models import Horario
from gestionarPlanMedicion.models import PlanMedicionCurso


@login_required(login_url='login')
def evidenciasxHorario(request, id_curso, id_horario):

    tiene_evidencias = False
    # curso = Curso.objects.get(pk=id_curso)
    horario = Horario.objects.get(pk=id_horario)
    plan_medicion_curso = PlanMedicionCurso.objects.get(pk=horario.curso_id)
    semestre = plan_medicion_curso.semestre
    curso = Curso.objects.get(pk=plan_medicion_curso.curso_id)

    listaEvidencias = EvidenciasxHorario.objects.filter(horario_id=id_horario, estado=1)
    if (len(listaEvidencias) > 0):
        tiene_evidencias = True
    context = {
        'curso': curso,
        'horario': horario,
        'listaEvidencias': listaEvidencias,
        'tiene_evidencias': tiene_evidencias,
        'semestre':semestre,
        'media_path': MEDIA_URL
    }
    return render(request, 'gestionarEvidencias/evidenciasxHorario.html', context)


def subirEvidenciaxHorario(request):
    descripcion = request.POST['descripcion']
    concepto = request.POST['concepto']
    archivo = request.FILES['archivo']
    horario = Horario.objects.get(pk=request.POST['horariopk'])
    evidencia = EvidenciasxHorario.objects.create(horario=horario, archivo=archivo, concepto=concepto,
                                                  descripcion=descripcion)
    ser_instance = serializers.serialize('json', [evidencia, ])
    return JsonResponse({"nuevaEvidencia": ser_instance}, status=200)


def editarEvidenciaxHorario(request):
    evidencia = EvidenciasxHorario.objects.get(pk=request.POST['evidenciapk'])
    varFlag =0
    nuevoArchivo = 0
    try:
        nuevoArchivo = request.FILES['archivoMod']
    except:
        varFlag=1

    nuevaDescripcion = request.POST['descripcionMod']
    nuevoConcepto = request.POST['conceptoMod']

    if varFlag==0:
        evidencia.archivo = nuevoArchivo
    evidencia.concepto = nuevoConcepto
    evidencia.descripcion = nuevaDescripcion
    evidencia.save()
    return JsonResponse({}, status=200)


def eliminarEvidenciaxHorario(request):
    print(request.POST)
    pk = request.POST['evidenciapk']
    evidencia = EvidenciasxHorario.objects.get(pk=pk)
    evidencia.estado = '0'  # eliminaci??n l??gica
    evidencia.save()
    return JsonResponse({}, status=200)


def listarEvidencias(request):
    id_horario = request.POST['horariopk']
    listaEvidencias = EvidenciasxHorario.objects.filter(horario_id=id_horario, estado=1)
    print(listaEvidencias)
    ser_instance = serializers.serialize('json', list(listaEvidencias), fields=('id', 'horario', 'archivo', 'concepto', 'descripcion' ))
    return JsonResponse({"listaEvidencias": ser_instance}, status=200)
