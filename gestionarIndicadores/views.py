import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers
# Create your views here.
from gestionarIndicadores.models import Indicador
from gestionarNivel.models import Nivel
from gestionarResultados.models import ResultadoPUCP


def editarIndicador(request, pk):
    flag = False
    if request.POST:
        indicador = Indicador.objects.get(pk=pk)
        indicador.codigo = request.POST['codigo']
        indicador.descripcion = request.POST['descripcion']
        indicador.save()
        flag = True

    indicador = Indicador.objects.get(pk=pk)
    id_resultado= indicador.resultado_id
    nivelLista = Nivel.objects.filter(state=1)
    context = {
        'indicador': indicador,
        'flag': flag,
        'id_resultado' : id_resultado,
        'nivelLista':nivelLista,
    }
    return render(request, 'gestionarIndicadores/editarIndicador.html', context)


def listarIndicadorxResultado(request,id_resultado):
    flag = False
    if request.POST:
        indicador = Indicador.objects.get(pk=request.POST['indicadorPK'])
        indicador.estado = 0  #eliminación lógica
        indicador.save()
        flag = True

    listaIndicadores = Indicador.objects.filter()
    context = {
        'listaIndicadores': listaIndicadores,
        'flag': flag
    }
    return render(request, 'gestionarIndicadores/listarIndicadorxResultado.html', context)


def agregarIndicador(request, id_resultado):
    codigo = request.POST['codigoI']
    descripcion = request.POST['descripcionI']
    resultado = ResultadoPUCP.objects.get(pk=id_resultado)
    indicador = Indicador.objects.create(codigo=codigo, descripcion=descripcion, resultado=resultado)
    ser_instance = serializers.serialize('json', [indicador, ])
    return JsonResponse({"nuevoIndicador": ser_instance}, status=200)

