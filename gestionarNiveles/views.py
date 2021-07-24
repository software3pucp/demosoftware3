from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core import serializers
from django.contrib.auth.decorators import login_required
from gestionarEspecialidad.models import Especialidad, Asistente, Auditor
from gestionarFacultad.models import Facultad
from gestionarNiveles.models import Nivel
from django.contrib.auth.models import Group

from gestionarResultados.models import PlanResultados


@login_required
def niveles(request):
    especialidades = []
    facultades = []

    if (request.user.rol_actual == "Asistente de acreditación"):
        usuario = request.user
        especialidades = []
        items = Asistente.objects.filter(user_id=usuario.pk)
        for item in items:
            especialidades.append(item.especialidad)
        context = {
            'especialidades': especialidades,
        }
        return render(request, 'gestionarNiveles/nivelesCE.html', context)

    if (request.user.rol_actual == "Auditor"):
        usuario = request.user
        especialidades = []
        items = Auditor.objects.filter(user_id=usuario.pk)
        for item in items:
            especialidades.append(item.especialidad)
        context = {
            'especialidades': especialidades,
        }
        return render(request, 'gestionarNiveles/nivelesCE.html', context)

    if (request.user.rol_actual == "Coordinador de facultad"):
        usuario = request.user
        grupo = Group.objects.get(pk=4)
        facultades = Facultad.objects.filter(responsable=usuario.pk)
        context = {
            'facultades': facultades,
        }
        return render(request, 'gestionarNiveles/nivelesCF.html', context)

    if (request.user.rol_actual == "Coordinador de especialidad"):
        usuario = request.user
        grupo = Group.objects.get(pk=5)
        especialidades = Especialidad.objects.filter(responsable=usuario.pk)
        context = {
            'especialidades': especialidades,
        }
        return render(request, 'gestionarNiveles/nivelesCE.html', context)



def obtenerEspecialidades(request):
    print(request.POST)
    id_facultad = request.POST['facultadpk']
    especialidades = Especialidad.objects.filter(facultad_id=id_facultad, estado='1')
    data = serializers.serialize("json", especialidades)
    return JsonResponse({"resp": data}, status=200)


def listarNiveles(request):
    id_especialidad = request.POST['especialidadpk']
    plan = PlanResultados.objects.get(estado='1', especialidad_id=id_especialidad)
    niveles = Nivel.objects.filter(especialidad_id=id_especialidad, estado='1',plaResultado_id=plan.pk).order_by('valor')
    ser_instance = serializers.serialize('json', niveles)
    return JsonResponse({"niveles": ser_instance}, status=200)

@login_required
def editarNivel(request):
    pk = request.POST['nivelpk']
    nivel = Nivel.objects.get(pk=pk)
    nivel.nombre = request.POST['nombreNivelMod']
    nivel.valor = request.POST['valorNivelMod']
    nivel.save()
    return JsonResponse({}, status=200)


def eliminarNivel(request):
    id_nivel = request.POST['nivelpk']
    nivel = Nivel.objects.get(pk=id_nivel)
    nivel.estado = '0'  # eliminación lógica
    nivel.save()
    return JsonResponse({}, status=200)


def crearNivel(request):
    id_especialidad = request.POST['especialidadpk']

    print(id_especialidad)
    try:
        especialidad = Especialidad.objects.get(pk=id_especialidad)
    except:
        print("Error al buscar la especialidad")

    plan = PlanResultados.objects.get(estado='1',especialidad_id=id_especialidad)

    nombre = request.POST['nombreNivel']
    valor = request.POST['valorNivel']
    nivel = Nivel.objects.create(nombre=nombre, valor=valor, especialidad=especialidad,plaResultado_id=plan.pk)
    ser_instance = serializers.serialize('json', [nivel, ])
    return JsonResponse({"nuevoNivel": ser_instance}, status=200)
