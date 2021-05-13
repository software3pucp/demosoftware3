from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
# Create your views here.
from datetime import datetime
from gestionarSemestre.models import Semestre

def listarSemestre(request):
    semestreLista = reversed(Semestre.objects.filter())
    context = {
        'ListaSemestre':semestreLista
    }
    return render(request, 'gestionarSemestre/listarSemestre.html', context)

def agregarSemestre(request):
    anho = int(request.POST["nombreCodigo"][0:4])
    etapa = int(request.POST["nombreCodigo"][5:6])
    meses = {
        "01": "Enero",
        "02": "Febrero",
        "03": "Marzo",
        "04": "Abril",
        "05": "Mayo",
        "06": "Junio",
        "07": "Julio",
        "08": "Agosto",
        "09": "Septiembre",
        "10": "Octubre",
        "11": "Noviembre",
        "12": "Diciembre",
    }

    fechaIni = request.POST["inicio"][0:2] + " de "+meses[request.POST["inicio"][3:5]]
    fechaFin = request.POST["fin"][0:2] + " de "+meses[request.POST["fin"][3:5]]
    semestre = Semestre.objects.create(nombreCodigo=request.POST["nombreCodigo"], anho=anho,
                            etapa=etapa, inicio=fechaIni, fin=fechaFin)
    ser_instance = serializers.serialize('json', [semestre,])
    return JsonResponse({"nuevoSemestre": ser_instance}, status=200)

def enviarCursoHorario(request,nombreCodigo):
    semestre = Semestre.objects.get(nombreCodigo=nombreCodigo)
    context = {
        "semestreSeleccionado": semestre
    }
    return  render(request, 'gestionarSemestre/semestre/semestreDetalle.html', context)
