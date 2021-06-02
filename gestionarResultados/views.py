import requests

from django.shortcuts import render, redirect
from django.db.models import Q
# Create your views here.
from gestionarIndicadores.models import Indicador
from gestionarResultados.models import ResultadoPUCP


def crearResultado(request):
    registrado = False
    if request.POST:
        newResultado = ResultadoPUCP.objects.create(codigo=request.POST['codigo'],
                                                    descripcion=request.POST['descripcion'])
        return redirect('listarResultado')

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

    context = {
        'resultados': listaResultados,
    }
    return render(request, 'gestionarResultados/listarResultados.html', context)


def editarResultado(request,pk):
    if request.POST:
        resultado = ResultadoPUCP.objects.get(pk=pk)
        resultado.codigo = request.POST['codigo']
        resultado.descripcion = request.POST['descripcion']
        resultado.save()
        return redirect('listarResultado')

    resultado = ResultadoPUCP.objects.get(pk=pk)
    listaIndicares = Indicador.objects.filter(resultado_id=pk, estado=1)
    context = {
        'listaIndicadores': listaIndicares,
        'resultado':resultado,
    }
    return render(request, 'gestionarResultados/editarResultado.html', context)
