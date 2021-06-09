from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse

# Create your views here.
from gestionarHorario.models import Horario
from gestionarSemestre.models import Semestre


def resultadosMediciones(request):

    if request.POST:
        if request.POST['operacion'] == 'agregar':
            xValues = Horario.objects.filter(responsable=1)
            yValues = Semestre.objects.filter(etapa=1)
            dataX = serializers.serialize("json", xValues)
            dataY = serializers.serialize("json", yValues)
            return JsonResponse({"xLabel": dataX, "yLabel": dataY}, status=200)

    context = {

    }
    return render(request,'gestionarResultadosMediciones/resultadosMediciones.html',context)