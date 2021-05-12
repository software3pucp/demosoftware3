from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.template.loader import render_to_string
from gestionarEspecialidad.models import Especialidad



# Create your views here.
def listarEspecialidad(request):
    especialidadLista = reversed(Especialidad.objects.filter())
    context = {
        'ListaEspecialidad': especialidadLista
    }
    return render(request, 'gestionarEspecialidad/listarEspecialidad.html', context)


def agregarEspecialidad(request):
    nombre = int(request.POST["nombre"][0:4])
    responsable = int(request.POST["responable"][5:6])
    foto = int(request.POST["foto"][5:6])
    especialidad = Especialidad.objects.create(nombre=nombre, responsable=responsable,
                                               foto=foto, inicio=request.POST["inicio"], fin=request.POST["fin"])
    ser_instance = serializers.serialize('json', [especialidad, ])
    return JsonResponse({"nuevaEspecialidad": ser_instance}, status=200)
