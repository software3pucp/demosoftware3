import json
from django.core import serializers
from django.http import JsonResponse


from django.shortcuts import render, redirect
from django.db.models import Q
# Create your views here.
from gestionarEspecialidad.models import Especialidad
from gestionarFacultad.models import Facultad
from gestionarIndicadores.models import Indicador
from gestionarResultados.models import ResultadoPUCP, PlanResultados
from django.contrib.auth.decorators import login_required

from gestionarSemestre.models import Semestre


@login_required
def crearResultado(request, id_especialidad,id_plan):
    especialidad = Especialidad.objects.get(pk=id_especialidad)
    if request.POST:
        codigo = request.POST['codigo']
        descripcion = request.POST['descripcion']
        newResultado = ResultadoPUCP.objects.create(codigo= codigo, descripcion=descripcion, especialidad=especialidad)
        return redirect('resultados',id_plan)

    context = {
        'especialidad': especialidad,
        'plan': id_plan,
    }
    return render(request, 'gestionarResultados/crearResultado.html', context)

@login_required
def Resultados(request, pk_plan):
    plan = PlanResultados.objects.get(pk=pk_plan)
    especialidadSeleccionada = Especialidad.objects.get(pk=plan.especialidad_id)
    facultadSeleccionada = Facultad.objects.get(pk=especialidadSeleccionada.facultad_id)
    facultades = Facultad.objects.filter(estado='1')
    context = {
        'facultades': facultades,
        'facultadSeleccionada': facultadSeleccionada,
        'especialidadSeleccionada': especialidadSeleccionada,
        'plan': plan
    }

    print(context)
    print()
    print()
    print()
    print()
    print()
    print()
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
def editarResultado(request,pk,id_plan):
    if request.POST:
        resultado = ResultadoPUCP.objects.get(pk=pk)
        resultado.codigo = request.POST['codigo']
        resultado.descripcion = request.POST['descripcion']
        resultado.save()
        return redirect('resultados', id_plan)

    resultado = ResultadoPUCP.objects.get(pk=pk)
    listaIndicares = Indicador.objects.filter(resultado_id=pk, estado=1)
    context = {
        'listaIndicadores': listaIndicares,
        'resultado':resultado,
        'plan': id_plan
    }
    return render(request, 'gestionarResultados/editarResultado.html', context)

@login_required
def planDeResultado(request):
    facultades = Facultad.objects.filter(estado='1')
    context = {
        'facultades': facultades,
    }
    return render(request, 'gestionarResultados/planDeResultado.html', context)

def crearPlanResultado(request,id_especialidad):
    try:
        especialidad = Especialidad.objects.get(pk=id_especialidad)
    except:
        print("Error al buscar la especialidad")

    if request.POST:
        codigo = request.POST['codigo']
        nombre = request.POST['nombre']
        nuevoPlanResultado = PlanResultados.objects.create(codigo=codigo, descripcion=nombre , especialidad=especialidad,estado='2')
        return redirect('planDeResultado')

    context = {
        'especialidad': especialidad,
    }
    return render(request, 'gestionarResultados/crearPlanDeResultado.html', context)

def listarPlanResultado(request):

    id_especialidad = request.POST['especialidad']

    planes = PlanResultados.objects.filter(especialidad_id=id_especialidad).exclude(estado=0)
    listaHistorico = []
    # lista2 = []
    for plan in planes:
        tiene_resultados = False
        # indicadores = Indicador.objects.filter(resultado_id=result.pk, estado='1')
        # if (len(indicadores) > 0):
        #     tiene_indicadores = True
        # else:
        #     tiene_indicadores = False
        registro = [plan, tiene_resultados]
        listaHistorico.append(registro)
        # lista2.append(tiene_indicadores)

    ser_instance = serializers.serialize('json', planes)
    # ser_instance2 = json.dumps(lista2)
    # ser_instance2 = serializers.serialize('json', listaResultados)
    # ,"tiene_niveles": ser_instance2
    return JsonResponse({"planes": ser_instance}, status=200)

def activarPlan(request):
    plan = PlanResultados.objects.get(pk=request.POST["planResultadoPk"])
    #planes = PlanResultados.objects.filter(especialidad_id=request.POST["especialidad"])
    planes = PlanResultados.objects.filter(especialidad_id=request.POST["especialidad"]).exclude(estado=0)
    planes.update(estado='2')
    plan.estado = '1'
    plan.save()
    return JsonResponse({}, status=200)

def desactivarPlan(request):
    plan = PlanResultados.objects.get(pk=request.POST["planResultadoPk"])
    plan.estado = '2'
    plan.save()
    return JsonResponse({}, status=200)

def editarPlanDeResultado(request,pk):
    if request.POST:
        plan = PlanResultados.objects.get(pk=pk)
        plan.codigo = request.POST['codigo']
        plan.descripcion = request.POST['descripcion']
        plan.save()
        return redirect('planDeResultado')
    context = {
        'plan': pk
    }
    return render(request, 'gestionarResultados/editarPlanDeResultado.html', context)

def eliminarPlanResultado(request):
    planPk = request.POST['planResultadoPk']
    plan = PlanResultados.objects.get(pk=planPk)
    plan.estado = '0'  # eliminación lógica
    plan.save()
    #plan.delete()
    return JsonResponse({}, status=200)

