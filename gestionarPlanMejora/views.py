import json

from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.db.models import Q

# Create your views here.
from authentication.views import Show
from demosoftware3.settings import MEDIA_URL
from gestionarPlanMejora.models import EstadoActividad, PropuestaMejora, ActividadMejora, EvidenciaActividadMejora, \
    ResponsableMejora
from django.http import JsonResponse
from authentication.models import User

# Create your views here.
from django.core import serializers
from gestionarCurso.models import Curso
from gestionarEspecialidad.models import Especialidad
from gestionarFacultad.models import Facultad
from gestionarHorario.models import Horario
from gestionarIndicadores.models import Indicador
from gestionarPlanMejora.models import PlanMejora
from django.contrib.auth.decorators import login_required


def crearActividad(request, id_propuesta):  # quizas sea necesario pasar como parámetro el pk del plan de mejora
    estado = EstadoActividad()
    try:
        estado = EstadoActividad.objects.get(pk=1)  # estado registrado
    except:
        print("no se encontro un estado")

    propuestaMejora = PropuestaMejora.objects.get(pk=id_propuesta)
    inicio = 2021  # año de inicio de la actividad
    fin = 2021  # año de fin de la actividad

    if request.POST:  # creación por metodo POST
        codigo = request.POST['codigo']
        descripcion = request.POST['descripcion']
        actividad = ActividadMejora.objects.create(codigo=codigo, descripcion=descripcion,
                                                   propuestaMejora=propuestaMejora, estado=estado,
                                                   inicio=inicio, fin=fin)
        responsables = request.POST.getlist('choices-multiple-remove-button')
        print(responsables)
        for val in responsables:
            user = User.objects.get(id=val)
            ResponsableMejora.objects.create(actividad=actividad, responsable=user)
        return redirect('editarPropuesta', pk=propuestaMejora.pk)

    if request.POST:
        if request.POST['operacion'] == 'listEspe':
            especialidades = Especialidad.objects.filter(facultad_id=request.POST['facultad'], estado='1')
            data = serializers.serialize("json", especialidades)
            return JsonResponse({"resp": data}, status=200)
        elif request.POST['operacion'] == 'listCur':
            planes = PlanMejora.objects.filter(curso__especialidad_id__exact=request.POST['especialidad'])
            pks = planes.values_list('curso_id', flat=True)
            cursos = Curso.objects.filter(pk__in=pks)
            dataP = serializers.serialize("json", planes)
            dataC = serializers.serialize("json", cursos)
            return JsonResponse({"resp": dataP, "resp1": dataC}, status=200)
        elif request.POST['operacion'] == 'eliminar':
            planMedicion = PlanMejora.objects.get(pk=request.POST['planPk'])
            planMedicion.delete()
            # print(planMedicion)

    facultades = Facultad.objects.filter()
    especialidades = Especialidad.objects.filter()  # TODO::: Verificar si se usa "Especialidades" en el template gestionarPlanMedicion/listarPlanMedicion
    print(especialidades)
    estados = PlanMejora.ESTADOS[1:]

    context = {
        'users': User.objects.all(),
        'grupos': Group.objects.all(),
        'propuesta': propuestaMejora,
    }
    return render(request, 'gestionarPlanMejora/crearActividad.html', context)


def editarActividad(request, pk):
    media_path = MEDIA_URL
    if request.POST:
        actividad = ActividadMejora.objects.get(pk=pk)
        actividad.codigo = request.POST['codigo']
        actividad.descripcion = request.POST['descripcion']
        idEstado = request.POST['cboEstado']
        nuevoEstado = EstadoActividad.objects.get(pk=idEstado)
        actividad.estado = nuevoEstado
        if request.POST.getlist('choices-multiple-remove-button-2'):
            actividad.groups.clear()
            responsables = request.POST.getlist('choices-multiple-remove-button-2')
            for val in responsables:
                user = User.objects.get(id=val)
                ResponsableMejora.objects.create(actividad=actividad, responsable=user)
            actividad.save()
        return redirect('')  # regresa a la pagina anterior

    actividad = ActividadMejora.objects.get(pk=pk)
    propuestapk = actividad.propuestaMejora_id
    propuesta = PropuestaMejora.objects.get(pk=propuestapk)

    estados = EstadoActividad.objects.filter()
    listaEvidencias = EvidenciaActividadMejora.objects.filter(actividad_id=pk, estado='1')
    responsables = ResponsableMejora.objects.filter(actividad_id=pk)

    lresponsables = []
    nlresponsables = []
    print("===============RESPONSABLES==============")
    print(responsables)
    print(nlresponsables)
    for rs in responsables:
        lresponsables.append(User.objects.get(pk=rs.responsable_id))

    print(lresponsables)
    context = {
        'listaEvidencias': listaEvidencias,
        'actividad': actividad,
        'estados': estados,
        'media_path': media_path,
        'responsables': lresponsables,
        'nresponsables': nlresponsables,
        'users': User.objects.all(),
        'propuesta': propuesta,
    }
    return render(request, 'gestionarPlanMejora/editarActividad.html', context)


def subirEvidencia(request, id_actividad):
    media_path = MEDIA_URL
    actividad = ActividadMejora.objects.get(pk=id_actividad)

    if request.POST:  # subir evidencia por método POST
        descripcion = request.POST['descripcion']
        concepto = request.POST['concepto']
        archivo = request.FILES['archivo']
        EvidenciaActividadMejora.objects.create(descripcion=descripcion, concepto=concepto,
                                                archivo=archivo, actividad=actividad)
        return redirect('editarActividad', pk=id_actividad)

    context = {
        'actividad': actividad,
        'media_path': media_path,
    }
    return render(request, 'gestionarPlanMejora/subirEvidencia.html', context)


def editarEvidencia(request, pk):
    media_path = MEDIA_URL
    if request.POST:
        descripcion = request.POST['descripcion']
        concepto = request.POST['concepto']
        archivo = request.FILES['archivo']

        evidencia = EvidenciaActividadMejora.objects.get(pk=pk)
        id_actividad = evidencia.actividad_id
        evidencia.descripcion = descripcion
        evidencia.concepto = concepto
        evidencia.archivo = archivo
        evidencia.save()
        return redirect('editarActividad', pk=id_actividad)

    evidencia = EvidenciaActividadMejora.objects.get(pk=pk)
    id_actividad = evidencia.actividad_id
    context = {
        'media_path': media_path,
        'evidencia': evidencia,
        'id_actividad': id_actividad,
    }
    return render(request, 'gestionarPlanMejora/editarEvidencia.html', context)


def editarPropuesta(request, pk):
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<')
    print(pk)
    propuestaMejora = PropuestaMejora.objects.get(pk=pk)
    listaActividades = ActividadMejora.objects.filter(propuestaMejora_id=pk, activo=1)
    if request.POST:
        propuestaMejora = PropuestaMejora.objects.get(pk=pk)
        propuestaMejora.codigo = request.POST['codigo']
        propuestaMejora.descripcion = request.POST['descripcion']
        propuestaMejora.save()
        id_planmejora = propuestaMejora.planMejora_id
        planMejora = PlanMejora.objects.get(pk=id_planmejora)
        id_medicion = planMejora.planMedicion.pk

        return redirect('planMejora', pk=id_medicion)

    print('-------------------------------------------------------------------------------------------')
    print(listaActividades)
    context = {
        'listaActividades': listaActividades,
        'propuestaMejora': propuestaMejora,
    }
    return render(request, 'gestionarPlanMejora/propuestaMejora.html', context)


def eliminarEvidenciaxActividad(request):
    evidenciapk = request.POST['evidenciapk']
    evidencia = EvidenciaActividadMejora.objects.get(pk=evidenciapk)
    evidencia.estado = '0'
    evidencia.save()
    return JsonResponse({}, status=200)


def planMejora(request, pk):
    if pk != "0":
        planMejora = PlanMejora.objects.get(pk=pk)
        print(planMejora)
    facultades = Facultad.objects.filter(estado='1')
    context = {
        'facultades': facultades,
        'planmejora': planMejora,
    }
    return render(request, 'gestionarPlanMejora/planMejora.html', context)


def eliminarPropuesta(request):
    propuestapk = request.POST['propuestapk']
    propuesta = PropuestaMejora.objects.get(pk=propuestapk)
    propuesta.estado = '0'  # eliminación lógica
    propuesta.save()
    return JsonResponse({}, status=200)


def filtrarEspecialidades(request):
    id_facultad = request.POST['facultad']
    especialidades = Especialidad.objects.filter(facultad_id=id_facultad, estado='1')
    data = serializers.serialize("json", especialidades)
    return JsonResponse({"resp": data}, status=200)


def listarPropuestas(request):
    idEspecialidad = request.POST['especialidad']
    print('------------------------------------------')
    print(idEspecialidad)
    print('-------------------------------------------')

    propuestas = PropuestaMejora.objects.filter(especialidad_id=idEspecialidad, estado='1')
    listaPropuestas = []
    lista2 = []  # lista para saber si tiene o no actividades de mejorar asociadas
    for propuesta in propuestas:
        tiene_actividades = False
        actividades = ActividadMejora.objects.filter(propuestaMejora_id=propuesta.pk, estado='1')
        if (len(actividades) > 0):
            tiene_actividades = True
        else:
            tiene_actividades = False

        lista2.append(tiene_actividades)

    ser_instance = serializers.serialize('json', propuestas)
    ser_instance2 = json.dumps(lista2)

    return JsonResponse({"propuestas": ser_instance, "tiene_actividades": ser_instance2}, status=200)


@login_required
def crearPlanMejora(request, pk):
    insert = False
    # El flag 0: operacion no realizada
    # flag > 0: operacion correspondiente realizada
    flag = 0
    errorInsert = 0
    plan = PlanMejora()
    plan.pk = pk
    listaCursos = []
    listaEstados = PlanMejora.ESTADOS[1:]
    listaHorarios = []
    listaIndicadores = Indicador.objects.filter()
    especialidad = ''
    horariosSelec = []
    indicadoresSelec = []
    if request.POST:
        if request.POST['operacion'] == 'editar':
            flag = 1
        elif request.POST['operacion'] == 'insertar':
            planes = PlanMejora.objects.filter(curso_id=request.POST['curso'])
            if len(planes) == 0:
                PlanMejora.objects.create(curso_id=request.POST['curso'], estado=request.POST['estado'])
                plan = PlanMejora.objects.latest('id')
                pk = plan.pk
                flag = 2
            else:
                errorInsert = 1
        listaCursos = Curso.objects.filter(especialidad=request.POST['especialidad'])
        especialidad = Especialidad.objects.get(pk=request.POST['especialidad'])

    if pk == '0':
        insert = True
    else:
        plan = PlanMejora.objects.get(pk=pk)
        manyInd = plan.indicador.all()
        manyHor = plan.horario.all()
        indicadoresSelec = manyInd
        horariosSelec = manyHor

    context = {
        'especialidad': especialidad,
        'listaCursos': listaCursos,
        'listaHorarios': listaHorarios,
        'listaEstados': listaEstados,
        'listaIndicadores': listaIndicadores,
        'horariosSelec': horariosSelec,
        'indicadoresSelec': indicadoresSelec,
        'plan': plan,
        'insert': insert,
        'flag': flag,
        'errorInsert': errorInsert,
    }
    return render(request, 'gestionarPlanMejora/crearPlanMejora.html', context)


def crearPropuesta(request, id_planmejora):
    planMejora = PlanMejora.objects.get(pk=id_planmejora)
    especialidad = Especialidad.objects.get(pk=planMejora.especialidad.pk)

    if request.POST:
        codigo = request.POST['codigo']
        descripcion = request.POST['descripcion']
        PropuestaMejora.objects.create(codigo=codigo, descripcion=descripcion,
                                       especialidad=especialidad, estado=1, planMejora=planMejora)
        return redirect('planMejora', pk=planMejora.planMedicion_id)

    context = {
        'especialidad': especialidad,
        'planMejora': planMejora
    }
    return render(request, 'gestionarPlanMejora/crearPropuesta.html', context)


def eliminarActividadxPropuesta(request):
    actividadpk = request.POST['epk']
    print("**********")
    print(actividadpk)
    print("**********")
    actividad = ActividadMejora.objects.get(pk=actividadpk)
    actividad.activo = '0'  # eliminación lógica
    actividad.save()
    return JsonResponse({}, status=200)


def crearAjax(request):
    if request.POST:
        if request.POST['operacion'] == 'listHorarios':
            listaHorarios = Horario.objects.filter(curso_id=request.POST['curso'])
            data = serializers.serialize("json", listaHorarios)
            return JsonResponse({"resp": data}, status=200)
        elif request.POST['operacion'] == 'mostrarHorario':
            data = request.POST['horarioPk']
            return JsonResponse({"resp": data}, status=200)
        elif request.POST['operacion'] == 'mostrarIndicador':
            indicador = Indicador.objects.filter(pk=request.POST["indicadorPk"])
            data = serializers.serialize("json", indicador)
            return JsonResponse({"resp": data}, status=200)
        elif request.POST['operacion'] == 'agregarIndicador':
            indicador = Indicador.objects.filter(pk=request.POST["indicadorPk"])
            plan = PlanMejora.objects.get(pk=request.POST["planPK"])
            indicadores = plan.indicador.all()
            if indicador[0] in indicadores:
                return JsonResponse({'status': 'false', 'message': 'Indicador ya ingresado'}, status=500)
            plan.indicador.add(indicador[0].pk)
            data = serializers.serialize("json", indicador)
            return JsonResponse({"resp": data}, status=200)
        elif request.POST['operacion'] == 'quitarIndicador':
            indicador = Indicador.objects.filter(pk=request.POST["indicadorPk"])
            plan = PlanMejora.objects.get(pk=request.POST["planPK"])
            indicadores = plan.indicador.all()
            if indicador[0] not in indicadores:
                return JsonResponse({'status': 'false', 'message': 'Indicador ya ingresado'}, status=500)
            plan.indicador.remove(indicador[0].pk)
            data = serializers.serialize("json", indicador)
            return JsonResponse({"resp": data}, status=200)
        elif request.POST['operacion'] == 'agregarHorario':
            horario = Horario.objects.filter(pk=request.POST["horarioPk"])
            plan = PlanMejora.objects.get(pk=request.POST["planPK"])
            horarios = plan.horario.all()
            if horario[0] in horarios:
                return JsonResponse({'status': 'false', 'message': 'Horario ya ingresado'}, status=500)
            plan.horario.add(horario[0].pk)
            data = serializers.serialize("json", horario)
            return JsonResponse({"resp": data}, status=200)
        elif request.POST['operacion'] == 'quitarHorario':
            horario = Horario.objects.filter(pk=request.POST["horarioPk"])
            plan = PlanMejora.objects.get(pk=request.POST["planPK"])
            horarios = plan.horario.all()
            if horario[0] not in horarios:
                return JsonResponse({'status': 'false', 'message': 'Indicador ya ingresado'}, status=500)
            plan.horario.remove(horario[0].pk)
            data = serializers.serialize("json", horario)
            return JsonResponse({"resp": data}, status=200)
