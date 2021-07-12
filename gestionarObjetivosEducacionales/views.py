from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
# Create your views here.
from gestionarEspecialidad.models import Especialidad, Auditor, Asistente
from django.contrib.auth.models import Group

from gestionarFacultad.models import Facultad
from gestionarObjetivosEducacionales.models import ObjetivoEducacional


@login_required
def objetivos(request):
    especialidades = []
    facultades=[]

    if (request.user.rol_actual == "Asistente de acreditación"):
        usuario = request.user
        especialidades = []
        items = Asistente.objects.filter(user_id=usuario.pk)
        for item in items:
            especialidades.append(item.especialidad)
        context = {
            'especialidades': especialidades,
        }
        return render(request, 'gestionarObjetivosEducacionales/objetivosEducacionalesCE.html', context)

    if (request.user.rol_actual == "Auditor"):
        usuario = request.user
        especialidades = []
        items = Auditor.objects.filter(user_id=usuario.pk)
        for item in items:
            especialidades.append(item.especialidad)
        context = {
            'especialidades': especialidades,
        }
        return render(request, 'gestionarObjetivosEducacionales/objetivosEducacionalesCE.html', context)

    if (request.user.rol_actual == "Coordinador de facultad"):
        usuario = request.user
        grupo = Group.objects.get(pk=4)
        facultades = Facultad.objects.filter(responsable=usuario.pk)
        context = {
            'facultades': facultades,
        }
        return render(request, 'gestionarObjetivosEducacionales/objetivosEducacionalesCF.html', context)

    if (request.user.rol_actual == "Coordinador de especialidad"):
        usuario = request.user
        grupo = Group.objects.get(pk=5)
        especialidades = Especialidad.objects.filter(responsable=usuario.pk)
        context = {
            'especialidades': especialidades,
        }
        return render(request, 'gestionarObjetivosEducacionales/objetivosEducacionalesCE.html', context)



def listarObjetivos(request):
    id_especialidad = request.POST['especialidad']
    objetivos = ObjetivoEducacional.objects.filter(especialidad_id=id_especialidad).exclude(estado=0)
    ser_instance = serializers.serialize('json', objetivos)
    return JsonResponse({"objetivos": ser_instance}, status=200)


def crearObjetivo(request):
    id_especialidad = request.POST['especialidadpk']
    especialidad = Especialidad.objects.get(pk=id_especialidad)
    codigo = request.POST['codigo']
    descripcion = request.POST['descripcion']
    objetivo = ObjetivoEducacional.objects.create(codigo=codigo, descripcion=descripcion, especialidad=especialidad)
    ser_instance = serializers.serialize('json', [objetivo, ])
    return JsonResponse({"nuevoObjetivo": ser_instance}, status=200)


def editarObjetivo(request):
    pk = request.POST['objetivopk']
    objetivo = ObjetivoEducacional.objects.get(pk=pk)
    objetivo.codigo = request.POST['codigoObjetivoMod']
    objetivo.descripcion = request.POST['descripcionObjetivoMod']
    objetivo.save()
    ser_instance = serializers.serialize('json', [objetivo, ])
    return JsonResponse({"objetivoEditado": ser_instance}, status=200)


def eliminarObjetivo(request):
    objetivopk = request.POST['objetivopk']
    objetivo = ObjetivoEducacional.objects.get(pk=objetivopk)
    objetivo.estado = '0'  # eliminación lógica
    objetivo.save()
    return JsonResponse({}, status=200)


def obtEspecialidades(request):
    id_facultad = request.POST['facultad']
    especialidades = Especialidad.objects.filter(facultad_id=id_facultad, estado='1')
    data = serializers.serialize("json", especialidades)
    return JsonResponse({"resp": data}, status=200)
