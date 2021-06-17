import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.core import serializers
from gestionarCurso.models import Curso
from gestionarEspecialidad.models import Especialidad
from gestionarFacultad.models import Facultad
from gestionarHorario.models import Horario
from gestionarIndicadores.models import Indicador
from gestionarPlanMedicion.models import PlanMedicion, PlanMedicionCurso
from django.contrib.auth.decorators import login_required
from gestionarSemestre.models import Semestre

@login_required
def listarPlanMedicion(request):

    especialidad = Especialidad()
    semestre = Semestre()
    planMedicion = PlanMedicion()
    if request.POST:
        if request.POST['operacion'] == 'entrada':
            print('***************************************************************************************************')
            print(request.POST)
            print('***************************************************************************************************')
            especialidad = Especialidad.objects.get(pk=request.POST['especialidad'])
            semestre = Semestre.objects.get(pk=request.POST['semestre'])
            planMedicion = PlanMedicion.objects.get(pk=request.POST['planMedicion'])
        elif request.POST['operacion'] == 'listEspe':
            especialidades = Especialidad.objects.filter(facultad_id=request.POST['facultad'], estado='1')
            data = serializers.serialize("json", especialidades)
            return JsonResponse({"resp": data}, status=200)
        elif request.POST['operacion'] == 'listCur':
            planes = PlanMedicionCurso.objects.filter(curso__especialidad_id__exact=request.POST['especialidad'],estado = request.POST['estado'])
            pks = planes.values_list('curso_id',flat=True)
            cursos = Curso.objects.filter(pk__in=pks)
            dataP = serializers.serialize("json", planes)
            dataC = serializers.serialize("json", cursos)
            return JsonResponse({"resp": dataP,"resp1": dataC}, status=200)
        elif request.POST['operacion'] == 'estado':
            planMedicionCurso = PlanMedicionCurso.objects.get(pk=request.POST['planpk'])
            if planMedicionCurso.estado == '1':
                planMedicionCurso.estado = '2'
            elif planMedicionCurso.estado == '2':
                planMedicionCurso.estado = '1'
            planMedicionCurso.save()


    facultades = Facultad.objects.filter()
    especialidades = Especialidad.objects.filter() # TODO::: Verificar si se usa "Especialidades" en el template gestionarPlanMedicion/listarPlanMedicion
    print(especialidades)
    estados = PlanMedicionCurso.ESTADOS[1:]
    context = {
        'facultades' : facultades,
        'especialidades' : especialidades,
        'planMedicion' : planMedicion,
        'especialidad' : especialidad,
        'semestre' : semestre,
        'estados' : estados,
    }
    return render(request,'gestionarPlanMedicion/listarPlanMedicion.html',context)

@login_required
def crearPlanMedicion(request,pk):
    insert = False
    #El flag 0: operacion no realizada
    #flag > 0: operacion correspondiente realizada
    flag = 0
    errorInsert = 0
    plan = PlanMedicionCurso()
    plan.pk = pk
    listaCursos = []
    listaEstados = PlanMedicionCurso.ESTADOS[1:]
    listaHorarios = []
    listaIndicadores = Indicador.objects.filter()
    especialidad = ''
    semestre = ''
    planMedicion = ''
    horariosSelec = []
    indicadoresSelec = []
    if request.POST:
        if request.POST['operacion'] == 'entrada':
            especialidad = Especialidad.objects.get(pk=request.POST['especialidad'])
            semestre = Semestre.objects.get(pk=request.POST['semestre'])
            planMedicion = PlanMedicion.objects.get(pk=request.POST['planMedicion'])
        elif request.POST['operacion'] == 'editar':
            flag = 1
        elif request.POST['operacion'] == 'insertar':
            print('***************************************************************************************************')
            print(request.POST)
            print('***************************************************************************************************')
            planes = PlanMedicionCurso.objects.filter(curso_id=request.POST['curso'])
            if len(planes) == 0:
                PlanMedicionCurso.objects.create(curso_id=request.POST['curso'],planMedicion_id=request.POST['planMedicion'],semestre_id=request.POST['semestre'],estado=request.POST['estado'])
                plan = PlanMedicionCurso.objects.latest('id')
                pk = plan.pk
                flag = 2
            else:
                errorInsert = 1
        listaCursos = Curso.objects.filter(especialidad=request.POST['especialidad'])


    if pk == '0':
        insert = True
    else:
        plan = PlanMedicionCurso.objects.get(pk=pk)
        manyInd = plan.indicador.all()
        manyHor = plan.horario.all()
        indicadoresSelec = manyInd
        horariosSelec = manyHor

    context = {
        'listaCursos': listaCursos,
        'listaHorarios': listaHorarios,
        'listaEstados': listaEstados,
        'listaIndicadores': listaIndicadores,
        'horariosSelec': horariosSelec,
        'indicadoresSelec': indicadoresSelec,
        'planMedicion': planMedicion,
        'especialidad': especialidad,
        'semestre': semestre,
        'plan': plan,
        'insert': insert,
        'flag': flag,
        'errorInsert': errorInsert,
    }
    return render(request,'gestionarPlanMedicion/crearPlanMedicion.html',context)

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
            plan = PlanMedicionCurso.objects.get(pk=request.POST["planPK"])
            indicadores = plan.indicador.all()
            if indicador[0] in indicadores:
                return JsonResponse({'status':'false','message':'Indicador ya ingresado'}, status=500)
            plan.indicador.add(indicador[0].pk)
            data = serializers.serialize("json", indicador)
            return JsonResponse({"resp": data}, status=200)
        elif request.POST['operacion'] == 'quitarIndicador':
            indicador = Indicador.objects.filter(pk=request.POST["indicadorPk"])
            plan = PlanMedicionCurso.objects.get(pk=request.POST["planPK"])
            indicadores = plan.indicador.all()
            if indicador[0] not in indicadores:
                return JsonResponse({'status': 'false', 'message': 'Indicador ya ingresado'}, status=500)
            plan.indicador.remove(indicador[0].pk)
            data = serializers.serialize("json", indicador)
            return JsonResponse({"resp": data}, status=200)
        elif request.POST['operacion'] == 'agregarHorario':
            horario = Horario.objects.filter(pk=request.POST["horarioPk"])
            plan = PlanMedicionCurso.objects.get(pk=request.POST["planPK"])
            horarios = plan.horario.all()
            if horario[0] in horarios:
                return JsonResponse({'status':'false','message':'Horario ya ingresado'}, status=500)
            plan.horario.add(horario[0].pk)
            data = serializers.serialize("json", horario)
            return JsonResponse({"resp": data}, status=200)
        elif request.POST['operacion'] == 'quitarHorario':
            horario = Horario.objects.filter(pk=request.POST["horarioPk"])
            plan = PlanMedicionCurso.objects.get(pk=request.POST["planPK"])
            horarios = plan.horario.all()
            if horario[0] not in horarios:
                return JsonResponse({'status': 'false', 'message': 'Indicador ya ingresado'}, status=500)
            plan.horario.remove(horario[0].pk)
            data = serializers.serialize("json", horario)
            return JsonResponse({"resp": data}, status=200)


def historico(request):
    facultades = Facultad.objects.filter(estado='1')
    context = {
        'facultades': facultades,
    }

    return render(request, 'gestionarPlanMedicion/listarMediciones.html', context)

def crearHistorico(request, id_especialidad):
    try:
        especialidad = Especialidad.objects.get(pk=id_especialidad)
    except:
        print("Error al buscar la especialidad")

    if request.POST:
        codigo = request.POST['codigo']
        nombre = request.POST['nombre']
        nuevoHistorico = PlanMedicion.objects.create(codigo=codigo,nombre=nombre, especialidad=especialidad,estado='1')
        return redirect('historico')

    context = {
        'especialidad': especialidad,
    }
    return render(request, 'gestionarPlanMedicion/crearPlanMedicionHistorico.html', context)

def listarHistorico(request):
    id_especialidad = request.POST['especialidad']
    historicos = PlanMedicion.objects.filter(especialidad_id=id_especialidad, estado=1)
    listaHistorico = []
    #lista2 = []
    for historico in historicos:
        tiene_semestres = False
        # indicadores = Indicador.objects.filter(resultado_id=result.pk, estado='1')
        # if (len(indicadores) > 0):
        #     tiene_indicadores = True
        # else:
        #     tiene_indicadores = False
        registro = [historico, tiene_semestres]
        listaHistorico.append(registro)
        #lista2.append(tiene_indicadores)

    ser_instance = serializers.serialize('json', historicos)
    #ser_instance2 = json.dumps(lista2)
    #ser_instance2 = serializers.serialize('json', listaResultados)
    #,"tiene_niveles": ser_instance2
    return JsonResponse({"historicos": ser_instance}, status=200)

def eliminarMedicion(request):
    historicoPk = request.POST['historicoPk']
    historico = PlanMedicion.objects.get(pk=historicoPk)
    historico.estado = '0'  # eliminación lógica
    historico.save()
    return JsonResponse({}, status=200)

def editarHistorico(request,pk):
    listaSemestre = reversed(Semestre.objects.filter())
    historico = PlanMedicion.objects.get(pk=pk)
    manySemestre = historico.semestre.all()
    semestresSeleccionados = reversed(manySemestre)
    especialidad = Especialidad.objects.get(pk=historico.especialidad_id)
    context = {
        'listaSemestre': listaSemestre,
        'historico': historico,
        'especialidad': especialidad,
        'semestresSeleccionados': semestresSeleccionados,
    }
    return render(request, 'gestionarPlanMedicion/editarPlanMedicionHistorico.html', context)

def agregarSemestrePlan(request):
    historico = PlanMedicion.objects.get(pk=request.POST['historicoPK'])
    semestre = Semestre.objects.get(pk=request.POST['semestrePk'])
    historico.semestre.add(semestre)
    ser_instance = serializers.serialize('json', [semestre, ])
    print(historico.semestre.all().count())
    print("////////////////////////////////////Se agrego 1////////////////////////////////////////")
    return JsonResponse({"semestreAgregado": ser_instance}, status=200)

def eliminarSemestrePlan(request):
    semestre = Semestre.objects.filter(pk=request.POST['semestrePk'])
    historico = PlanMedicion.objects.get(pk=request.POST['historicoPK'])
    semestres = historico.semestre.all()
    if semestre[0] not in semestres:
        return JsonResponse({'status': 'false', 'message': 'Semestre ya ingresado'}, status=500)
    historico.semestre.remove(semestre[0].pk)
    data = serializers.serialize("json", semestre)
    print(historico.semestre.all().count())
    print("////////////////////////////////////Se quito 1////////////////////////////////////////")
    return JsonResponse({"resp": data}, status=200)

def editarNombre(request):
    historico = PlanMedicion.objects.get(pk=request.POST['historicoPK'])
    historico.nombre = request.POST['nombre']
    historico.codigo = request.POST['codigo']
    historico.save()
    return JsonResponse({}, status=200)