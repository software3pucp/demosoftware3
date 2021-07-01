import json

from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
from gestionarCurso.models import Curso
from gestionarEvaluacion.models import RespuestaEvaluacion
from gestionarHorario.models import Horario
from gestionarNiveles.models import Nivel
from gestionarPlanMedicion.models import PlanMedicionCurso
from gestionarSemestre.models import Semestre


@login_required
def resultadosMediciones(request):
    print('***************************************************************************************************')
    print(request.POST)
    print('***************************************************************************************************')
    if request.POST:
        if request.POST['operacion'] == 'agregar':
            if(request.POST['curso'] == ''):
                return
            curso = PlanMedicionCurso.objects.get(pk=request.POST['curso'])
            niveles = Nivel.objects.filter(especialidad_id=curso.curso.especialidad_id,estado='1')
            horarios = Horario.objects.filter(curso_id=request.POST['curso'],estado='1')
            listaHor = []
            for horario in horarios:
                listaNiv = []
                for nivel in niveles:
                    c = RespuestaEvaluacion.objects.filter(valorNota=nivel.valor,horario_id=horario.pk).count()
                    jsonNivel = {"nivel": nivel.valor, "cant": c}
                    listaNiv.append(jsonNivel)
                jsonHor = {"horario": horario.codigo, "notas": listaNiv}
                listaHor.append(jsonHor)
            resCur = {"nombre": curso.curso.nombre,"horarios":listaHor}
            dataX = serializers.serialize("json", horarios)
            return JsonResponse({"xLabel": dataX, "yLabel": resCur}, status=200)

        elif request.POST['operacion'] == 'actualizarCursos':
            cursos = list(PlanMedicionCurso.objects.filter(semestre_id=request.POST['semestre'],estado='1'))
            data = []
            for cur in cursos:
                jsonCurso = {"pk": cur.pk, "curso": cur.curso.nombre}
                data.append(jsonCurso)
            print({"resp": data})
            return JsonResponse({"resp": data}, status=200)

    semestres = Semestre.objects.filter();
    context = {
        'semestres': semestres,
    }
    return render(request,'gestionarResultadosMediciones/resultadosMediciones.html',context)