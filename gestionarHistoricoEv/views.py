from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
# Create your views here.
from datetime import datetime
from gestionarHistoricoEv.models import Historico
from gestionarHorario.models import Horario
from gestionarCurso.models import Curso
from gestionarEvidencias.models import EvidenciasxHorario
from demosoftware3.settings import MEDIA_URL
from itertools import chain
def listarHistorico(request,pk):
    media_path = MEDIA_URL
    cursoSeleccionado = Curso.objects.get(pk=pk)
    listaHorarios = list(Horario.objects.filter(curso_id=pk,estado=1))
    #listaDocumentos = EvidenciasxHorario.objects.filter(estado=1)
    listaDocumentos = EvidenciasxHorario.objects.none()
    for i in range(len(listaHorarios)):
        listaEDocumentos = EvidenciasxHorario.objects.filter(horario_id=listaHorarios[i].id, estado=1)
        if listaEDocumentos:
            listaDocumentos = listaDocumentos|listaEDocumentos

    context = {
       # 'ListaHistorico':historicoLista,
        'cursoSeleccionado': cursoSeleccionado,
        'listaDocumentos': listaDocumentos
    }
    return render(request, 'gestionarHistoricoEv/listarHistorico.html', context)