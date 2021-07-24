import json
from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.db.models import Q
# Create your views here.
from gestionarEspecialidad.models import Especialidad, Auditor, Asistente
from gestionarFacultad.models import Facultad
from gestionarIndicadores.models import Indicador
from gestionarNiveles.models import Nivel
from gestionarResultados.models import ResultadoPUCP, PlanResultados
from django.contrib.auth.decorators import login_required

from gestionarRubrica.models import Rubrica
from gestionarSemestre.models import Semestre

@login_required
def validarCrear(request):
    id_plan = int(request.POST['idPlan'])
    if request.POST:
        if id_plan == -1:
            print(id_plan)
             #Si no existe plan de resultados se debe mostrar mensaje informativo
            return JsonResponse({'tipo':'1'},status=200)
        else:
            #TODO
            # Si el plan de resultados ya tiene asociado planes de medicion
            # Se debe mostar mensaje informativo
            return JsonResponse({'tipo':'3'},status =200)



@login_required
def crearResultado(request, id_plan):
    plan = PlanResultados.objects.get(pk=id_plan)
    especialidad = plan.especialidad
    if request.POST:
        codigo = request.POST['codigo']
        descripcion = request.POST['descripcion']
        ResultadoPUCP.objects.create(codigo=codigo, descripcion=descripcion, planResultado=plan)
        return redirect('resultados', id_plan=id_plan)

    context = {
        'plan': plan,
    }
    return render(request, 'gestionarResultados/crearResultado.html', context)


@login_required
def Resultados(request, id_plan):
    plan = PlanResultados.objects.get(pk=id_plan)
    especialidad = plan.especialidad
    context = {
        'plan': plan,
        'especialidad': especialidad,
    }
    return render(request, 'gestionarResultados/resultados.html', context)

def resultadosActivos(request):

    if (request.user.rol_actual == "Asistente de acreditación"):
        usuario = request.user
        especialidades = []
        items = Asistente.objects.filter(user_id=usuario.pk)
        for item in items:
            especialidades.append(item.especialidad)
        context = {
            'especialidades': especialidades,
        }
        return render(request, 'gestionarResultados/resultadosActivosCE.html', context)

    if (request.user.rol_actual == "Auditor"):
        usuario = request.user
        especialidades = []
        items = Auditor.objects.filter(user_id=usuario.pk)
        for item in items:
            especialidades.append(item.especialidad)
        context = {
            'especialidades': especialidades,
        }
        return render(request, 'gestionarResultados/resultadosActivosCE.html', context)

    if (request.user.rol_actual == "Coordinador de facultad"):
        usuario = request.user
        grupo = Group.objects.get(pk=4)
        facultades = Facultad.objects.filter(responsable=usuario.pk, estado='1')
        context = {
            'facultades': facultades,
        }
        return render(request, 'gestionarResultados/resultadosActivosCF.html', context)

    if (request.user.rol_actual == "Coordinador de especialidad"):
        usuario = request.user
        grupo = Group.objects.get(pk=5)
        especialidades = Especialidad.objects.filter(responsable=usuario.pk, estado='1')
        context = {
            'especialidades': especialidades,
        }
        return render(request, 'gestionarResultados/resultadosActivosCE.html', context)

def duplicarPlan(request):

    planPk = 1

    # Duplicado del plan de resultados seleccionado
    plan = PlanResultados.objects.get(pk=planPk)
    _plan = PlanResultados.objects.get(pk=plan.pk)
    _plan.pk = None
    _plan.save()
    # Desactivando plan de resultados seleccionado
    plan.estado = '2'
    plan.save()

    # Duplicado de niveles del plan de resultados seleccionado
    niveles = Nivel.objects.filter(plaResultado_id=plan.pk,estado='1')
    for nivel in niveles:
        _nivel = Nivel.objects.get(pk=nivel.pk)
        _nivel.pk = None
        _nivel.plaResultado_id  =_plan.pk
        _nivel.save()
    _niveles = Nivel.objects.filter(plaResultado_id=_plan.pk)

    resultados = ResultadoPUCP.objects.filter(planResultado_id=planPk,estado ='1')
    for resultado in resultados:
        #Duplicado del resultado actual
        _resultado = ResultadoPUCP.objects.get(pk=resultado.pk)
        _resultado.pk = None
        _resultado.planResultado_id = _plan.pk
        _resultado.save()
        indicadores = Indicador.objects.filter(resultado_id=resultado.pk,estado='1')
        for indicador in indicadores:
            #Duplicado del indicador actual
            _indicador = Indicador.objects.get(pk=indicador.pk)
            _indicador.pk = None
            _indicador.resultado_id = _resultado.pk
            _indicador.save()
            for i in range(len(niveles)):
                try:
                    rubrica = Rubrica.objects.get(nivel_id=niveles[i].pk,indicador_id=indicador.pk)
                    _rubrica = Rubrica.objects.get(pk=rubrica.pk)
                    _rubrica.pk = None
                    _rubrica.nivel_id=_niveles[i].pk
                    _rubrica.indicador_id=_indicador.pk
                    _rubrica.save()
                except:
                    print("Nivel no tiene asociado una rúbrica")





    return redirect('resultadosActivos')

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
    especialidadpk = request.POST['especialidad']
    idPlan = -1
    plan = PlanResultados.objects.filter(especialidad_id=especialidadpk, estado=1)
    resultados = []
    lista2= []
    if (plan):
        idPlan = plan[0].pk
        resultados = ResultadoPUCP.objects.filter(planResultado_id=idPlan, estado=1)
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
    # ser_instance2 = serializers.serialize('json', listaResultados)
    return JsonResponse({"resultados": ser_instance, "tiene_niveles": ser_instance2,"idPlan":idPlan}, status=200)

def listarResultadosHistoricos(request):
    planpk = request.POST['planpk']
    resultados = ResultadoPUCP.objects.filter(planResultado_id=planpk, estado=1)
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
    # ser_instance2 = serializers.serialize('json', listaResultados)
    return JsonResponse({"resultados": ser_instance, "tiene_niveles": ser_instance2}, status=200)


@login_required
def editarResultado(request, pk):
    resultado = ResultadoPUCP.objects.get(pk=pk)
    plan = resultado.planResultado
    if request.POST:
        resultado = ResultadoPUCP.objects.get(pk=pk)
        resultado.codigo = request.POST['codigo']
        resultado.descripcion = request.POST['descripcion']
        resultado.save()
        return redirect('resultados', id_plan=plan.pk)

    listaIndicares = Indicador.objects.filter(resultado_id=pk, estado=1)
    context = {
        'listaIndicadores': listaIndicares,
        'resultado': resultado,
        'plan':plan,
    }
    return render(request, 'gestionarResultados/editarResultado.html', context)


@login_required
def planDeResultado(request):
    if (request.user.rol_actual == "Asistente de acreditación"):
        usuario = request.user
        especialidades = []
        items = Asistente.objects.filter(user_id=usuario.pk)
        for item in items:
            especialidades.append(item.especialidad)
        context = {
            'especialidades': especialidades,
        }
        return render(request, 'gestionarResultados/planDeResultadosCE.html', context)

    if (request.user.rol_actual == "Auditor"):
        usuario = request.user
        especialidades = []
        items = Auditor.objects.filter(user_id=usuario.pk)
        for item in items:
            especialidades.append(item.especialidad)
        context = {
            'especialidades': especialidades,
        }
        return render(request, 'gestionarResultados/planDeResultadosCE.html', context)

    if (request.user.rol_actual == "Coordinador de facultad"):
        usuario = request.user
        grupo = Group.objects.get(pk=4)
        facultades = Facultad.objects.filter(responsable=usuario.pk, estado='1')
        context = {
            'facultades': facultades,
        }
        return render(request, 'gestionarResultados/planDeResultadosCF.html', context)

    if (request.user.rol_actual == "Coordinador de especialidad"):
        usuario = request.user
        grupo = Group.objects.get(pk=5)
        especialidades = Especialidad.objects.filter(responsable=usuario.pk, estado='1')
        context = {
            'especialidades': especialidades,
        }
        return render(request, 'gestionarResultados/planDeResultadosCE.html', context)



def crearPlanResultado(request, id_especialidad):
    try:
        especialidad = Especialidad.objects.get(pk=id_especialidad)
    except:
        print("Error al buscar la especialidad")

    if request.POST:
        codigo = request.POST['codigo']
        nombre = request.POST['nombre']
        nuevoPlanResultado = PlanResultados.objects.create(codigo=codigo, descripcion=nombre, especialidad=especialidad,
                                                           estado='2')
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
    # planes = PlanResultados.objects.filter(especialidad_id=request.POST["especialidad"])
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


def editarPlanDeResultado(request, pk):
    plan = PlanResultados.objects.get(pk=pk)
    if request.POST:
        plan = PlanResultados.objects.get(pk=pk)
        plan.codigo = request.POST['codigo']
        plan.descripcion = request.POST['descripcion']
        plan.save()
        return redirect('planDeResultado')
    context = {
        'plan': plan,
    }
    return render(request, 'gestionarResultados/editarPlanDeResultado.html', context)


def eliminarPlanResultado(request):
    planPk = request.POST['planResultadoPk']
    plan = PlanResultados.objects.get(pk=planPk)
    plan.estado = '0'  # eliminación lógica
    plan.save()
    # plan.delete()
    return JsonResponse({}, status=200)
