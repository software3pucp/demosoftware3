from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from gestionarCurso.models import Curso
from gestionarEvidencias.models import EvidenciasxHorario
from gestionarHorario.models import Horario


def listarEvidenciaHorario(request,id_curso,id_horario):

    if request.POST: # subir evidencia por método post
        archivo = request.FILES['archivo']
        horario = Horario.objects.get(pk=id_horario)
        EvidenciasxHorario.objects.create(horario=horario, evidencia=archivo)

    tiene_evidencias = False
    curso = Curso.objects.get(pk=id_curso)
    horario = Horario.objects.get(pk=id_horario)
    listaEvidencias = EvidenciasxHorario.objects.filter(horario_id=id_horario)
    if(len(listaEvidencias)>0):
        tiene_evidencias = True

    context = {
        'curso': curso,
        'horario': horario,
        'listaEvidencias': listaEvidencias,
        'tiene_evidencias': tiene_evidencias,
    }
    return render(request, 'gestionarEvidencias/listarEvidenciasHorario.html', context)


def editarEvidencia(request, pk):
    if request.POST:
        evidencia = EvidenciasxHorario.get(pk=pk)
        evidencia.archivo = request.FILES['archivo']
        evidencia.save()
        return redirect('listarEvidenciasHorario', pk=request.POST['horariopk'])

    evidencia = EvidenciasxHorario.objects.get(pk=pk)
    context = {
        'evidencia': evidencia,
    }
    return render(request, 'gestionarEvidencias/editarEvidencia.html', context)

def subirEvidenciaHorario(request):

    print(request.POST)
    print(request.FILES)

    archivo = request.FILES['archivo']
    horario = Horario.objects.get(pk=request.POST['horariopk'])
    evidencia = EvidenciasxHorario.objects.create(horario=horario, archivo=archivo)
    ser_instance = serializers.serialize('json', [evidencia, ])
    return JsonResponse({"nuevaEvidencia": ser_instance}, status=200)