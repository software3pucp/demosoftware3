import json

from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse

# Create your views here.
from gestionarCurso.models import Curso
from gestionarEvaluacion.models import RespuestaEvaluacion
from gestionarHorario.models import Horario
from gestionarNiveles.models import Nivel

def resultadosMediciones(request):

    if request.POST:
        if request.POST['operacion'] == 'agregar':
            curso = Curso.objects.get(pk=1)
            niveles = Nivel.objects.filter(especialidad_id=1)
            horarios = Horario.objects.filter(curso_id=1)
            listaHor = []
            for horario in horarios:
                listaNiv = []
                for nivel in niveles:
                    c = RespuestaEvaluacion.objects.filter(valorNota=nivel.valor,horario_id=horario.pk).count()
                    jsonNivel = {"nivel": nivel.valor, "cant": c}
                    listaNiv.append(jsonNivel)
                jsonHor = {"horario": horario.codigo, "notas": listaNiv}
                listaHor.append(jsonHor)
            resCur = {"nombre": curso.nombre,"horarios":listaHor}
            dataX = serializers.serialize("json", horarios)
            return JsonResponse({"xLabel": dataX, "yLabel": resCur}, status=200)

    context = {

    }
    return render(request,'gestionarResultadosMediciones/resultadosMediciones.html',context)