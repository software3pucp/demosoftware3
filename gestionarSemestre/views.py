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
    return render(request,'gestionarSemestre/listarSemestre.html',context)

def agregarSemestre(request):
    anho = int(request.POST["nombreCodigo"][0:4])
    etapa = int(request.POST["nombreCodigo"][5:6])
    semestre = Semestre.objects.create(nombreCodigo=request.POST["nombreCodigo"], anho=anho,
                            etapa=etapa, inicio=request.POST["inicio"], fin=request.POST["fin"])
    ser_instance = serializers.serialize('json', [semestre,])
    return JsonResponse({"nuevoSemestre": ser_instance}, status=200)