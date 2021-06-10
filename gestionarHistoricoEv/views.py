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
    listaNombres =[]
    for i in range(len(listaHorarios)):
        listaEDocumentos = EvidenciasxHorario.objects.filter(horario_id=listaHorarios[i].id, estado=1)
        if listaEDocumentos:
            aux = list(listaEDocumentos)
            for j in range(len(aux)):
                nombArchivo = str(aux[j].archivo)[8:]
                listaNombres.append(nombArchivo)
           # listaEDocumentos.update(archivo=nombArchivo)
            listaDocumentos = listaDocumentos|listaEDocumentos
    cantidad = len(listaNombres)
    nuevo = zip(listaNombres,listaDocumentos)
    r = set(nuevo)
    context = {
       # 'ListaHistorico':historicoLista,
        'cursoSeleccionado': cursoSeleccionado,
        'listaDocumentos': listaDocumentos,
        'listaNombres':listaNombres,
        'cantidad':cantidad,
        'listaAux':r,
    }
    return render(request, 'gestionarHistoricoEv/listarHistorico.html', context)