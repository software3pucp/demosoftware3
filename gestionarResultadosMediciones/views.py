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
from gestionarResultados.models import ResultadoPUCP
from gestionarSemestre.models import Semestre


@login_required
def resultadosMediciones(request,pk):

    plan = PlanMedicion.objects.get(pk=pk)
    indicadores = Indicador.objects.filter(resultado__planResultado_id=plan.planResultados_id)
    res = ResultadoPUCP.objects.filter(planResultado_id=plan.planResultados_id)
    niveles = Nivel.objects.filter(especialidad_id=plan.especialidad_id, estado='1')
    cantNiv = RespuestaEvaluacion.objects.filter(planMedicion__planMedicion_id=pk, estado='1').values(
        'valorNota').annotate(cant=Count('valorNota')).order_by('valorNota')

    progreIndicadores = []
    porcentajeAlumnosMedia = []
    cantNiveles = []
    progreResponsables = []
    progreREs = []

    et = RespuestaEvaluacion.objects.filter(planMedicion__planMedicion_id=pk, estado='1').values(
        'indicador').annotate(total=Count('indicador_id')).order_by('indicador_id')
    e = RespuestaEvaluacion.objects.filter(planMedicion__planMedicion_id=pk, calificado='1', evidencia='1',
                                           estado='1').values('indicador').annotate(
        total=Count('indicador_id')).order_by('indicador_id')

    mediana = 2
    mt = RespuestaEvaluacion.objects.filter(planMedicion__planMedicion_id=pk, calificado='1', evidencia='1',
                                           estado='1').values('indicador').annotate(
        total=Count('indicador_id')).order_by('indicador_id')
    m = RespuestaEvaluacion.objects.filter(planMedicion__planMedicion_id=pk, calificado='1', evidencia='1',
                                           valorNota__gt=mediana,
                                           estado='1').values('indicador').annotate(
        total=Count('indicador_id')).order_by('indicador_id')

    pt = RespuestaEvaluacion.objects.filter(planMedicion__planMedicion_id=pk,
                                            estado='1').values('indicador__resultado_id').annotate(
        total=Count('indicador__resultado_id')).order_by('indicador__resultado_id')

    p = RespuestaEvaluacion.objects.filter(planMedicion__planMedicion_id=pk, calificado='1', evidencia='1',
                                           estado='1').values('indicador__resultado_id').annotate(
        total=Count('indicador__resultado_id')).order_by('indicador__resultado_id')

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
        try:
            cant = cantNiv.get(valorNota=n.valor)['cant']
        except:
            cant = 0
        cantNiveles.append((n.nombre, cant))

    responsables = RespuestaEvaluacion.objects.filter(planMedicion__planMedicion_id=pk,estado='1').values("horario__responsable",
                                                                         "horario__responsable__first_name").annotate(
        total=Count("horario__responsable__first_name")).order_by()
    evaluados = RespuestaEvaluacion.objects.filter(estado='1', calificado="1", evidencia="1").values(
        "horario__responsable", "horario__responsable__first_name").annotate(
        total=Count("horario__responsable__first_name")).order_by()

    for r in responsables:
        try:
            por = round((evaluados.get(horario__responsable=r["horario__responsable"])['total'] /
                         responsables.get(horario__responsable=r["horario__responsable"])['total']) * 100)
        except:
            por = 0
        progreResponsables.append((r["horario__responsable__first_name"], por))

    for r in res:
        try:
            por = round((p.get(indicador__resultado_id=r.pk)['total'] /
                         pt.get(indicador__resultado_id=r.pk)['total']) * 100)
        except:
            por = 0
        progreREs.append((r,por))

    context = {
        'plan': plan,
        'indicadores': indicadores,
        'res': res,
        'progreResultados': progreREs,
        'porcentajeAlumnosMedia': porcentajeAlumnosMedia,
        'progreIndicadores': progreIndicadores,
        'cantNiveles': cantNiveles,
        'progreResponsables': progreResponsables,
    }
    return render(request, 'gestionarResultadosMediciones/resultadosMediciones.html', context)


@login_required
def getListaProgresoCurso(request):
    if request.POST:
        cursosTot = RespuestaEvaluacion.objects.filter(planMedicion__planMedicion_id=request.POST['planMedicion'],
                                                       indicador_id=request.POST['indicador'], estado='1').values(
            'planMedicion__curso').annotate(total=Count('planMedicion__curso')).order_by('planMedicion__curso')
        cursosCalif = RespuestaEvaluacion.objects.filter(planMedicion__planMedicion_id=request.POST['planMedicion'],
                                                         indicador_id=request.POST['indicador'], calificado='1',
                                                         evidencia='1', estado='1').values(
            'planMedicion__curso').annotate(total=Count('planMedicion__curso')).order_by('planMedicion__curso')
        progreCursos = []

        for curso in cursosTot:
            try:
                por = round((cursosCalif.get(planMedicion__curso=curso['planMedicion__curso'])['total'] /
                             curso['total']) * 100)
            except:
                por = 0
            cur = Curso.objects.get(pk=curso['planMedicion__curso'])
            progreCursos.append({"curso": cur.nombre, "porcentaje": por})

        return JsonResponse({"resp": progreCursos}, status=200)

@login_required
def getPorcentajeMedia(request):
    if request.POST:
        porcentajeMedia = []
        resultado = ResultadoPUCP.objects.get(pk=request.POST['RE'])
        plan = PlanMedicion.objects.get(pk=request.POST['planMedicion'], estado='1')
        indicadores = Indicador.objects.filter(resultado_id=request.POST['RE'])
        mediana = 2
        mt = RespuestaEvaluacion.objects.filter(planMedicion__planMedicion_id=plan.pk,
                                                calificado='1', evidencia='1',
                                                estado='1').values('indicador').annotate(
            total=Count('indicador_id')).order_by('indicador_id')
        m = RespuestaEvaluacion.objects.filter(planMedicion__planMedicion_id=plan.pk, valorNota__gt=mediana,
                                               calificado='1', evidencia='1',
                                               estado='1').values('indicador').annotate(
            total=Count('indicador_id')).order_by('indicador_id')
        for i in indicadores:
            try:
                por = round((m.get(indicador=i.pk)['total'] / mt.get(indicador=i.pk)['total']) * 100)
            except:
                por = 0
            porcentajeMedia.append({"indicador": i.descripcion, "porcentaje": por})

        print(porcentajeMedia)

        return JsonResponse({"resp": porcentajeMedia}, status=200)