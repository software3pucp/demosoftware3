import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
# Create your views here.
from django.core import serializers
from gestionarCurso.models import Curso
from gestionarEspecialidad.models import Especialidad
from gestionarFacultad.models import Facultad
from gestionarHorario.models import Horario
from gestionarIndicadores.models import Indicador
from gestionarPlanMedicion.models import PlanMedicion, PlanMedicionCurso
from django.contrib.auth.decorators import login_required

from gestionarPlanMejora.models import PlanMejora
from gestionarResultados.models import PlanResultados
from gestionarSemestre.models import Semestre
from authentication.models import User

@login_required
def listarPlanMedicion(request):

    especialidad = Especialidad()
    semestre = Semestre()
    planMedicion = PlanMedicion()
    planes = ''
    estado = ''
    if request.POST:
        if request.POST['operacion'] == 'entrada':
            especialidad = Especialidad.objects.get(pk=request.POST['especialidad'])
            semestre = Semestre.objects.get(pk=request.POST['semestre'])
            planMedicion = PlanMedicion.objects.get(pk=request.POST['planMedicion'])
        elif request.POST['operacion'] == 'estado':
            planMedicionCurso = PlanMedicionCurso.objects.get(pk=request.POST['planCurso'])
            if planMedicionCurso.estado == '1':
                planMedicionCurso.estado = '2'
            elif planMedicionCurso.estado == '2':
                planMedicionCurso.estado = '1'
            planMedicionCurso.save()

        elif request.POST['operacion'] == 'eliminar':
            planMedicionCurso = PlanMedicionCurso.objects.get(pk=request.POST['planCurso'])
            planMedicionCurso.estado = '0'
            planMedicionCurso.save()

        especialidad = Especialidad.objects.get(pk=request.POST['especialidad'])
        semestre = Semestre.objects.get(pk=request.POST['semestre'])
        planMedicion = PlanMedicion.objects.get(pk=request.POST['planMedicion'])
        planes = PlanMedicionCurso.objects.filter(planMedicion_id=planMedicion.pk, semestre_id=semestre.pk, estado=request.POST['estado'])
        estado = request.POST['estado']

    estados = PlanMedicionCurso.ESTADOS[1:]
    context = {
        'planes' : planes,
        'planMedicion' : planMedicion,
        'especialidad' : especialidad,
        'semestre' : semestre,
        'estados' : estados,
        'estadoSelec': estado,
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
    listaIndicadores = []
    especialidad = ''
    semestre = ''
    planMedicion = PlanMedicion.objects.get(pk=request.POST['planMedicion'])
    horariosSelec = []
    indicadoresSelec = []
    if request.POST:
        if request.POST['operacion'] == 'entrada':
            a=4 #Rellenar espacio
            # print('***************************************************************************************************')
            # print(request.POST)
            # print('***************************************************************************************************')
        elif request.POST['operacion'] == 'editar':
            flag = 1
        elif request.POST['operacion'] == 'insertar':
            # print('***************************************************************************************************')
            # print(request.POST)
            # print('***************************************************************************************************')
            planes = PlanMedicionCurso.objects.filter(curso_id=request.POST['curso'],planMedicion_id=request.POST['planMedicion'],semestre_id=request.POST['semestre']).exclude(estado=0)
            if len(planes) == 0:
                PlanMedicionCurso.objects.create(curso_id=request.POST['curso'],planMedicion_id=request.POST['planMedicion'],semestre_id=request.POST['semestre'],estado=request.POST['estado'])
                plan = PlanMedicionCurso.objects.latest('id')
                pk = plan.pk
                flag = 2
            else:
                errorInsert = 1
        especialidad = Especialidad.objects.get(pk=request.POST['especialidad'])
        semestre = Semestre.objects.get(pk=request.POST['semestre'])
        listaCursos = Curso.objects.filter(especialidad=request.POST['especialidad'])


    if pk == '0':
        insert = True
    else:
        plan = PlanMedicionCurso.objects.get(pk=pk)
        listaIndicadores = Indicador.objects.filter(resultado__planResultado__especialidad_id=request.POST['especialidad'],resultado__planResultado_id=planMedicion.planResultados_id, estado=1)
        manyInd = plan.indicador.all()
        manyHor = Horario.objects.filter(curso_id=pk,estado=1)
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
        'ListaUsuarios': User.objects.all(),
    }
    return render(request,'gestionarPlanMedicion/crearPlanMedicion.html',context)

def crearAjax(request):
    if request.POST:
        if request.POST['operacion'] == 'listHorarios':
            listaHorarios = Horario.objects.filter(curso_id=request.POST['curso'])
            data = serializers.serialize("json", listaHorarios)
            return JsonResponse({"resp": data}, status=200)
        elif request.POST['operacion'] == 'mostrarHorario':
            horario = Horario.objects.filter(pk=request.POST['horarioPk'])
            data = serializers.serialize("json", horario)
            # data = request.POST['horarioPk']
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
                return JsonResponse({'status': 'false', 'message': 'Indicador no encontrado'}, status=500)
            plan.indicador.remove(indicador[0].pk)
            data = serializers.serialize("json", indicador)
            return JsonResponse({"resp": data}, status=200)
        elif request.POST['operacion'] == 'agregarHorario':
            # print('***************************************************************************************************')
            # print(request.POST)
            # print('***************************************************************************************************')
            plan = PlanMedicionCurso.objects.get(pk=request.POST["planPK"])
            horarios = Horario.objects.filter(curso_id=request.POST["planPK"],estado=1)
            for horario in horarios:
                if horario.codigo == request.POST["codigo"]:
                    return JsonResponse({'status':'false','message':'Horario ya ingresado'}, status=500)

            Horario.objects.create(codigo=request.POST["codigo"],curso_id=request.POST["planPK"],responsable_id=request.POST["responsablePk"],estado=1)

            #insertar rol docente si es que no lo tiene
            user= User.objects.get(pk=request.POST["responsablePk"])
            group= Group.objects.get(name="Docente")
            userGroup = list(User.groups.through.objects.filter(user_id=request.POST["responsablePk"], group_id=group.pk))
            if len(userGroup) ==0:
                group.user_set.add(user)
                user.n_Roles = user.n_Roles + 1
                user.save()

            hor = Horario.objects.latest('id')
            horario = Horario.objects.filter(pk=hor.pk)
            data = serializers.serialize("json", horario)
            return JsonResponse({"resp": data}, status=200)
        elif request.POST['operacion'] == 'editarHorario':
            horario = Horario.objects.filter(pk=request.POST["horarioPk"])
            horarios = Horario.objects.filter(curso_id=request.POST["planPK"], estado=1)
            if horario[0] not in horarios:
                return JsonResponse({'status': 'false', 'message': 'Horario no encontrado'}, status=500)

            hor = Horario.objects.get(pk=request.POST["horarioPk"])
            group = Group.objects.get(name="Docente")

            #Quitar rol de docente a responsable si es necesario
            responsable = User.objects.get(pk=hor.responsable.pk)
            horarios = list(Horario.objects.filter(responsable=responsable.pk))
            if len(horarios) == 1:
                group.user_set.remove(responsable)
                responsable.n_Roles = responsable.n_Roles - 1
                responsable.save()

            hor.codigo = request.POST["codigo"]
            hor.responsable_id = request.POST["responsablePk"]
            hor.save()

            #Agregar rol de docente a nuevo responsable si es requerido
            user = User.objects.get(pk=request.POST["responsablePk"])
            userGroup = list(User.groups.through.objects.filter(user_id=request.POST["responsablePk"], group_id=group.pk))
            if len(userGroup) == 0:
                group.user_set.add(user)
                user.n_Roles = user.n_Roles + 1
                user.save()

            horario = Horario.objects.filter(pk=request.POST["horarioPk"])
            data = serializers.serialize("json", horario)
            return JsonResponse({"resp": data}, status=200)
        elif request.POST['operacion'] == 'quitarHorario':
            # print('***************************************************************************************************')
            # print(request.POST)
            # print('***************************************************************************************************')
            horario = Horario.objects.filter(pk=request.POST["horarioPk"])
            horarios = Horario.objects.filter(curso_id=request.POST["planPK"],estado=1)
            if horario[0] not in horarios:
                return JsonResponse({'status': 'false', 'message': 'Horario no encontrado'}, status=500)
            hor = Horario.objects.get(pk=request.POST["horarioPk"])

            #Quitar rol de docente si es necesario
            group = Group.objects.get(name="Docente")
            responsable = User.objects.get(pk=hor.responsable.pk)
            horarios = list(Horario.objects.filter(responsable=responsable.pk))
            if len(horarios) == 1:
                group.user_set.remove(responsable)

            hor.responsable_id = None
            hor.estado = 0
            hor.save()
            data = serializers.serialize("json", horario)
            return JsonResponse({"resp": data}, status=200)


def historico(request):
    especialidades = []
    facultades = []

    if request.POST:
        if request.POST['operacion'] == 'terminar':
            plan = PlanMedicion.objects.get(pk=request.POST['planMedicion'])
            plan.estado='2'
            plan.save()
            PlanMejora.objects.create(especialidad_id=plan.especialidad_id,planMedicion_id=plan.pk,estado=1)
            mejora = PlanMejora.objects.latest('id')
            return redirect('planMejora',pk=mejora.pk)
        if request.POST['operacion'] == 'ver plan':
            mejora = PlanMejora.objects.get(planMedicion_id=request.POST['planMedicion'],estado=1)
            return redirect('planMejora',pk=mejora.pk)

    if (request.user.rol_actual == "Coordinador de facultad"):
        usuario = request.user
        grupo = Group.objects.get(pk=4)
        facultades = Facultad.objects.filter(responsable=usuario.pk)
        context = {
            'facultades': facultades,
        }
        return render(request, 'gestionarPlanMedicion/listarMedicionesCF.html', context)

    if (request.user.rol_actual == "Coordinador de especialidad"):
        usuario = request.user
        grupo = Group.objects.get(pk=5)
        especialidades = Especialidad.objects.filter(responsable=usuario.pk)
        context = {
            'especialidades': especialidades,
        }
        return render(request, 'gestionarPlanMedicion/listarMedicionesCE.html', context)



def crearHistorico(request, id_especialidad):
    try:
        especialidad = Especialidad.objects.get(pk=id_especialidad)
    except:
        print("Error al buscar la especialidad")

    if request.POST:
        codigo = request.POST['codigo']
        nombre = request.POST['nombre']
        try:
            planResultado = PlanResultados.objects.get(especialidad_id=id_especialidad, estado=1)
        except:
            context = {
                'especialidad': especialidad,
                'error_message': 'No se tiene un Plan de Resultados activo para esta especialidad.',
            }
            return render(request, 'gestionarPlanMedicion/crearPlanMedicionHistorico.html', context)
        nuevoHistorico = PlanMedicion.objects.create(codigo=codigo,nombre=nombre, especialidad_id=id_especialidad, planResultados_id=planResultado.pk, estado='1')
        return redirect('historico')

    context = {
        'especialidad': especialidad,
    }
    return render(request, 'gestionarPlanMedicion/crearPlanMedicionHistorico.html', context)

def listarHistorico(request):
    id_especialidad = request.POST['especialidad']
    historicos = PlanMedicion.objects.filter(especialidad_id=id_especialidad, estado__gte='1')
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
    listaSemestre0 = (Semestre.objects.filter())
    listaSemestre =reversed(listaSemestre0)
    hay_semestres=False
    if (len(listaSemestre0)>0):
        hay_semestres = True

    historico = PlanMedicion.objects.get(pk=pk)
    manySemestre = historico.semestre.all()
    semestresSeleccionados = reversed(manySemestre)
    especialidad = Especialidad.objects.get(pk=historico.especialidad_id)
    context = {
        'listaSemestre': listaSemestre,
        'historico': historico,
        'especialidad': especialidad,
        'semestresSeleccionados': semestresSeleccionados,
        'hay_semestres':hay_semestres,
    }
    return render(request, 'gestionarPlanMedicion/editarPlanMedicionHistorico.html', context)

def agregarSemestrePlan(request):
    historico = PlanMedicion.objects.get(pk=request.POST['historicoPK'])
    semestre = Semestre.objects.get(pk=request.POST['semestrePk'])
    historico.semestre.add(semestre)
    ser_instance = serializers.serialize('json', [semestre, ])
    # print(historico.semestre.all().count())
    # print("////////////////////////////////////Se agrego 1////////////////////////////////////////")
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