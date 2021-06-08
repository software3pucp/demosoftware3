import requests
from django.core import serializers
from django.http import JsonResponse

from django.shortcuts import render, redirect
from django.db.models import Q
# Create your views here.
from gestionarEspecialidad.models import Especialidad
from gestionarFacultad.models import Facultad
from gestionarIndicadores.models import Indicador
from gestionarResultados.models import ResultadoPUCP


def crearResultado(request, id_especialidad):
    try:
        especialidad = Especialidad.objects.get(pk=id_especialidad)
    except:
        print("Error al buscar la especialidad")

    if request.POST:
        codigo = request.POST['codigo']
        descripcion = request.POST['descripcion']
        newResultado = ResultadoPUCP.objects.create(codigo= codigo, descripcion=descripcion, especialidad=especialidad)
        return redirect('resultados')

    context = {
        'especialidad': especialidad,
    }
    return render(request, 'gestionarResultados/crearResultado.html', context)


def Resultados(request):
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
        tiene_indicadores = False
        indicadores = Indicador.objects.filter(resultado_id=result.pk, estado='1')
        if(len(indicadores)>0):
            tiene_indicadores = True
        else:
            tiene_indicadores = False
        registro=[result,tiene_indicadores]
        listaResultados.append(registro)

    facultades = Facultad.objects.filter(estado='1')
    context = {
        'facultades': facultades,
        'resultados': listaResultados,
    }
    return render(request, 'gestionarResultados/resultados.html', context)


def obtenerEspecialidades(request):
    id_facultad = request.POST['facultad']
    especialidades = Especialidad.objects.filter(facultad_id=id_facultad, estado='1')
    data = serializers.serialize("json", especialidades)
    return JsonResponse({"resp": data}, status=200)


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
