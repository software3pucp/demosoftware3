import requests
from django.http import JsonResponse
from django.shortcuts import render

from django.core import serializers
from gestionarEspecialidad.models import Especialidad
from gestionarFacultad.models import Facultad
from gestionarREAcreditadoras.models import Acreditadora, ResultadoAcreditadora, REAcred_Indicador
from gestionarIndicadores.models import Indicador

# Create your views here.


def listarRE(request,pk):
    acreditadora = Acreditadora.objects.get(pk=pk)
    resultados = ResultadoAcreditadora.objects.filter(acreditadora=pk)
    context = {
        'acreditadora': acreditadora,
        'resultados' : resultados,
    }
    return render(request,'gestionarREAcreditadoras/listarRE.html',context)


def editarRE(request,pk):
    insert = False
    flag = 0
    indicadorSelec = []
    resultadoAcreditadora = ResultadoAcreditadora()
    resultadoAcreditadora.pk = pk
    facultades = Facultad.objects.filter()

    if request.POST:
        print(request.POST)
        if request.POST['operacion'] == 'entrada':
            resultadoAcreditadora.acreditadora_id = request.POST["acreditadora"]

        elif request.POST['operacion'] == 'editar':
            print('***************************************************************************************************')
            print(request.POST)
            print('***************************************************************************************************')
            flag = 1

        elif request.POST['operacion'] == 'insertar':
            print('***************************************************************************************************')
            print(request.POST)
            print('***************************************************************************************************')
            flag = 2

    if pk != '0':
        resultadoAcreditadora = ResultadoAcreditadora.objects.get(pk=pk)
        indicadorSelec = REAcred_Indicador.objects.filter(resultadoAcreditadora=pk)

    context = {
        'insert': insert,
        'indicadorSelec': indicadorSelec,
        'resultadoAcreditadora': resultadoAcreditadora,
        'facultades': facultades,
        'flag': flag,
    }
    return render(request,'gestionarREAcreditadoras/editarRE.html',context)

def eliminarRE(request,pk):

    #Candidate.objects.filter(pk=pk).delete()
    print(request.POST)
    return

def ajaxEditar(request):
    if request.POST:
        if request.POST['operacion'] == 'listEspe':
            especialidades = Especialidad.objects.filter(facultad_id=request.POST['facultad'])
            data = serializers.serialize("json", especialidades)
            return JsonResponse({"resp": data}, status=200)
        if request.POST['operacion'] == 'listIndi':
            indicadores = Indicador.objects.filter()
            data = serializers.serialize("json", indicadores)
            return JsonResponse({"resp": data}, status=200)
    return