import json

from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Count
# Create your views here.
import gestionarIndicadores.views
from gestionarCurso.models import Curso
from gestionarEspecialidad.models import Especialidad
from gestionarEvaluacion.models import RespuestaEvaluacion
from gestionarHorario.models import Horario
from gestionarIndicadores.models import Indicador
from gestionarNiveles.models import Nivel
from gestionarPlanMedicion.models import PlanMedicionCurso, PlanMedicion
from gestionarSemestre.models import Semestre


@login_required
def resultadosMediciones(request):
    if request.POST:
        if request.POST['operacion'] == 'agregar':
            if (request.POST['curso'] == ''):
                return
            curso = PlanMedicionCurso.objects.get(pk=request.POST['curso'])
            niveles = Nivel.objects.filter(especialidad_id=curso.curso.especialidad_id, estado='1')
            horarios = Horario.objects.filter(curso_id=request.POST['curso'], estado='1')
            listaHor = []
            for horario in horarios:
                listaNiv = []
                for nivel in niveles:
                    c = RespuestaEvaluacion.objects.filter(valorNota=nivel.valor, horario_id=horario.pk).count()
                    jsonNivel = {"nivel": nivel.valor, "cant": c}
                    listaNiv.append(jsonNivel)
                jsonHor = {"horario": horario.codigo, "notas": listaNiv}
                listaHor.append(jsonHor)
            resCur = {"nombre": curso.curso.nombre, "horarios": listaHor}
            dataX = serializers.serialize("json", horarios)
            return JsonResponse({"xLabel": dataX, "yLabel": resCur}, status=200)

        elif request.POST['operacion'] == 'actualizarCursos':
            cursos = list(PlanMedicionCurso.objects.filter(semestre_id=request.POST['semestre'], estado='1'))
            data = []
            for cur in cursos:
                jsonCurso = {"pk": cur.pk, "curso": cur.curso.nombre}
                data.append(jsonCurso)
            return JsonResponse({"resp": data}, status=200)
    especialidad = Especialidad.objects.get(pk=5)
    plan = RespuestaEvaluacion.objects.filter(planMedicion__planMedicion__estado='1',
                                              planMedicion__planMedicion__especialidad_id=especialidad.pk,
                                              estado='1').values('planMedicion__planMedicion__nombre').annotate(cant=Count('planMedicion__planMedicion__nombre')).order_by()
    semestres = Semestre.objects.filter()
    indicadores = Indicador.objects.filter(resultado__planResultado__estado='1')
    niveles = Nivel.objects.filter(especialidad_id='5', estado='1')
    cantNiv = RespuestaEvaluacion.objects.filter(planMedicion__planMedicion__estado='1',
                                                 planMedicion__planMedicion__especialidad_id=especialidad.pk, estado='1').values(
        'valorNota').annotate(cant=Count('valorNota')).order_by('valorNota')

    progreIndicadores = []
    porcentajeAlumnosMedia = []
    cantNiveles = []

    et = RespuestaEvaluacion.objects.filter(planMedicion__planMedicion__estado='1',
                                            planMedicion__planMedicion__especialidad_id=especialidad.pk, estado='1').values(
        'indicador').annotate(total=Count('indicador_id')).order_by('indicador_id')
    e = RespuestaEvaluacion.objects.filter(planMedicion__planMedicion__estado='1',
                                           planMedicion__planMedicion__especialidad_id=especialidad.pk, calificado='1', evidencia='1',
                                           estado='1').values('indicador').annotate(
        total=Count('indicador_id')).order_by('indicador_id')
    mediana = 2
    mt = RespuestaEvaluacion.objects.filter(planMedicion__planMedicion__estado='1',
                                           planMedicion__planMedicion__especialidad_id=especialidad.pk, calificado='1', evidencia='1',
                                           estado='1').values('indicador').annotate(
        total=Count('indicador_id')).order_by('indicador_id')
    m = RespuestaEvaluacion.objects.filter(planMedicion__planMedicion__estado='1', valorNota__gt=mediana,
                                           planMedicion__planMedicion__especialidad_id=especialidad.pk, calificado='1', evidencia='1',
                                           estado='1').values('indicador').annotate(
        total=Count('indicador_id')).order_by('indicador_id')

    for i in indicadores:
        try:
            por = round((e.get(indicador=i.pk)['total'] / et.get(indicador=i.pk)['total']) * 100)
        except:
            por = 0
        progreIndicadores.append((i, por))

        try:
            por = round((m.get(indicador=i.pk)['total'] / mt.get(indicador=i.pk)['total']) * 100)
        except:
            por = 0
        porcentajeAlumnosMedia.append((i,por))

    for n in niveles:
        cantNiveles.append((n.nombre, cantNiv.get(valorNota=n.valor)['cant']))

    responsables = RespuestaEvaluacion.objects.filter(estado='1').values("horario__responsable",
                                                                         "horario__responsable__first_name").annotate(
        total=Count("horario__responsable__first_name")).order_by()
    evaluados = RespuestaEvaluacion.objects.filter(estado='1', calificado="1", evidencia="1").values(
        "horario__responsable", "horario__responsable__first_name").annotate(
        total=Count("horario__responsable__first_name")).order_by()

    progreResponsables = []
    for r in responsables:
        try:
            por = round((evaluados.get(horario__responsable=r["horario__responsable"])['total'] /
                         responsables.get(horario__responsable=r["horario__responsable"])['total']) * 100)
        except:
            por = 0
        progreResponsables.append((r["horario__responsable__first_name"], por))
        print(plan)
    context = {
        'especialidad': especialidad,
        'plan': plan.get()['planMedicion__planMedicion__nombre'],
        'semestres': semestres,
        'indicadores': indicadores,
        'porcentajeAlumnosMedia': porcentajeAlumnosMedia,
        'progreIndicadores': progreIndicadores,
        'cantNiveles': cantNiveles,
        'progreResponsables': progreResponsables,
    }
    return render(request, 'gestionarResultadosMediciones/resultadosMediciones.html', context)


@login_required
def getListaProgresoCurso(request):
    if request.POST:
        especialidad = Especialidad.objects.get(pk=5)
        cursosTot = RespuestaEvaluacion.objects.filter(planMedicion__planMedicion__estado='1',indicador_id=request.POST['indicador'],
                                                    planMedicion__planMedicion__especialidad_id=especialidad.pk, estado='1').values(
            'planMedicion__curso').annotate(total=Count('planMedicion__curso')).order_by('planMedicion__curso')
        cursosCalif = RespuestaEvaluacion.objects.filter(planMedicion__planMedicion__estado='1',indicador_id=request.POST['indicador'],
                                                    planMedicion__planMedicion__especialidad_id=especialidad.pk, calificado='1',
                                                    evidencia='1', estado='1').values('planMedicion__curso').annotate(
            total=Count('planMedicion__curso')).order_by('planMedicion__curso')
        progreCursos = []

        for curso in cursosTot:
            try:
                por = round((cursosCalif.get(planMedicion__curso=curso['planMedicion__curso'])['total'] /
                             curso['total']) * 100)
            except:
                por = 0
            cur = Curso.objects.get(pk=curso['planMedicion__curso'])
            progreCursos.append({"curso": cur.nombre, "porcentaje": por})

        print(progreCursos)

        return JsonResponse({"resp": progreCursos}, status=200)
