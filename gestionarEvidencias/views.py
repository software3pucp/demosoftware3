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

@login_required(login_url='login')
def evidenciasxHorario(request, id_curso, id_horario):
    tiene_evidencias = False
    curso = Curso.objects.get(pk=id_curso)
    horario = Horario.objects.get(pk=id_horario)
    listaEvidencias = EvidenciasxHorario.objects.filter(horario_id=id_horario, estado=1)
    if (len(listaEvidencias) > 0):
        tiene_evidencias = True

    context = {
        'curso': curso,
        'horario': horario,
        'listaEvidencias': listaEvidencias,
        'tiene_evidencias': tiene_evidencias,
        'media_path': MEDIA_URL
    }
    return render(request, 'gestionarEvidencias/evidenciasxHorario.html', context)


def subirEvidenciaxHorario(request):
    print(request.POST)
    archivo = request.FILES['archivo']
    horario = Horario.objects.get(pk=request.POST['horariopk'])
    evidencia = EvidenciasxHorario.objects.create(horario=horario, archivo=archivo)
    ser_instance = serializers.serialize('json', [evidencia, ])
    return JsonResponse({"nuevaEvidencia": ser_instance}, status=200)

def editarEvidenciaxHorario(request):
    print('Editar evidencia------------------------------------')
    print(request.POST)
    print(request.FILES)
    # result = finders.find('css/theme.css')
    # searched_locations = finders.searched_locations
    # print(result)
    # print(searched_locations)
    print('----------------------------------------------------')


    evidencia = EvidenciasxHorario.objects.get(pk = request.POST['evidenciapk'])
    nuevoArchivo = request.FILES['archivoMod']
    evidencia.archivo = nuevoArchivo
    evidencia.save()
    return JsonResponse({},status=200)

def eliminarEvidenciaxHorario(request):
    print(request.POST)
    pk = request.POST['evidenciapk']
    evidencia = EvidenciasxHorario.objects.get(pk=pk)
    evidencia.estado = '0'  # eliminación lógica
    evidencia.save()
    return JsonResponse({},status=200)

def listarEvidencias(request):
    id_horario = request.POST['horariopk']
    listaEvidencias = EvidenciasxHorario.objects.filter(horario_id=id_horario, estado=1)
    ser_instance = serializers.serialize('json', list(listaEvidencias), fields=('id','horario','archivo'))
    return JsonResponse({"listaEvidencias":ser_instance}, status=200)
