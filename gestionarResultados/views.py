import json
from django.core import serializers
from django.http import JsonResponse


from django.shortcuts import render, redirect
from django.db.models import Q
# Create your views here.
from gestionarEspecialidad.models import Especialidad
from gestionarFacultad.models import Facultad
from gestionarIndicadores.models import Indicador
from gestionarResultados.models import ResultadoPUCP
from django.contrib.auth.decorators import login_required
@login_required
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

@login_required
def Resultados(request):

    facultades = Facultad.objects.filter(estado='1')
    context = {
        'facultades': facultades,
    }
    return render(request, 'gestionarResultados/resultados.html', context)

def eliminarResultado(request):
    resultadoPk = request.POST['resultadopk']
    resultado = ResultadoPUCP.objects.get(pk=resultadoPk)
    resultado.estado = '0'  # eliminación lógica
    resultado.save()
    return JsonResponse({}, status=200)


def obtenerEspecialidades(request):
    id_facultad = request.POST['facultad']
    especialidades = Especialidad.objects.filter(facultad_id=id_facultad, estado='1')
    data = serializers.serialize("json", especialidades)
    return JsonResponse({"resp": data}, status=200)

def listarResultados(request):
    id_especialidad = request.POST['especialidad']
    resultados = ResultadoPUCP.objects.filter(especialidad_id=id_especialidad, estado=1)
    listaResultados = []
    lista2 = []
    for result in resultados:
        tiene_indicadores = False
        indicadores = Indicador.objects.filter(resultado_id=result.pk, estado='1')
        if (len(indicadores) > 0):
            tiene_indicadores = True
        else:
            tiene_indicadores = False
        registro = [result, tiene_indicadores]
        listaResultados.append(registro)
        lista2.append(tiene_indicadores)

    ser_instance = serializers.serialize('json', resultados)
    ser_instance2 = json.dumps(lista2)
    #ser_instance2 = serializers.serialize('json', listaResultados)
    return JsonResponse({"resultados": ser_instance,"tiene_niveles": ser_instance2}, status=200)


@login_required
def editarResultado(request,pk):
    if request.POST:
        resultado = ResultadoPUCP.objects.get(pk=pk)
        resultado.codigo = request.POST['codigo']
        resultado.descripcion = request.POST['descripcion']
        resultado.save()
        return redirect('resultados')

    resultado = ResultadoPUCP.objects.get(pk=pk)
    listaIndicares = Indicador.objects.filter(resultado_id=pk, estado=1)
    context = {
        'listaIndicadores': listaIndicares,
        'resultado':resultado,
    }
    return render(request, 'gestionarResultados/editarResultado.html', context)
