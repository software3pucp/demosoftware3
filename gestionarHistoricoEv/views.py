from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
# Create your views here.
from datetime import datetime
from gestionarHistoricoEv.models import Historico
from gestionarHorario.models import Horario
from gestionarCurso.models import Curso
from demosoftware3.settings import MEDIA_URL
def listarHistorico(request,pk):
    media_path = MEDIA_URL
    #la lista debe ser por un horario de un curso en especifico
    historicoLista = reversed(Historico.objects.filter())
    cursoSeleccionado = Curso.objects.get(pk=pk)
    context = {
        'ListaHistorico':historicoLista,
        'cursoSeleccionado': cursoSeleccionado
    }
    return render(request, 'gestionarHistoricoEv/listarHistorico.html', context)