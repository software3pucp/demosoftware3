import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core import serializers
from django.db.models import Q
# Create your views here.
from gestionarIndicadores.models import Indicador
from gestionarNivel.models import Nivel
from gestionarResultados.models import ResultadoPUCP


def crearResultado(request):
    registrado = False
    if request.POST:
        newResultado = ResultadoPUCP.objects.create(codigo=request.POST['codigo'],
                                                    descripcion=request.POST['descripcion'])
        return redirect('editarResultado', pk=newResultado.pk)

    context = {
        'registrado': registrado,
    }
    return render(request, 'gestionarResultados/crearResultado.html', context)


def listarResultado(request):
    eliminado = False
    if request.POST:
        resultadoPk = request.POST['resultadoPk']
        resultado = ResultadoPUCP.objects.get(pk=resultadoPk)
        resultado.estado = '0'  # eliminación lógica
        resultado.save()
        eliminado = True

    resultados = ResultadoPUCP.objects.filter(Q(estado='1') | Q(estado='2'))
    listaResultados=[]
    for result in resultados:
        tiene_niveles = False
        indicadores = Indicador.objects.filter(resultado_id=result.pk)
        if(len(indicadores)>0):
            tiene_niveles=True
        registro=[result,tiene_niveles]
        listaResultados.append(registro)

    print("-------------------------")
    print(listaResultados)
    print("-------------------------")
    context = {
        'resultados': listaResultados,
    }
    return render(request, 'gestionarResultados/listarResultados.html', context)


def editarResultado(request, pk):
    context = {
        'listaIndicadores': Indicador.objects.filter(resultado_id=pk, estado=1),
        'listaResultado': ResultadoPUCP.objects.all(),
        'resultado': ResultadoPUCP.objects.get(pk=pk),
    }
    return render(request, 'gestionarIndicadores/listarIndicadorxResultado.html', context)


def actualizarResultado(request, pk):
    resultado = ResultadoPUCP.objects.get(pk=pk)
    resultado.codigo = request.POST['codigo']
    resultado.descripcion = request.POST['descripcion']
    resultado.save()
    ser_instance = serializers.serialize('json', [resultado, ])
    return JsonResponse({"resultadoActualizado": ser_instance}, status=200)
