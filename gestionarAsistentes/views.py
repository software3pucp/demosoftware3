from django.contrib.auth.models import Group
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.core import serializers
from authentication.models import User
from gestionarEspecialidad.models import Especialidad, Asistente


@login_required
def asistentes(request):
    especialidades = []

    if (request.user.rol_actual == "Coordinador de especialidad"):
        usuario = request.user
        grupo = Group.objects.get(name="Coordinador de especialidad")
        especialidades = Especialidad.objects.filter(responsable=usuario.pk)
    context = {
        'ListaUsuarios': User.objects.all(),
        'especialidades': especialidades,
    }
    return render(request, 'gestionarAsistentes/asistentes.html', context)


def registrarAsistente(request):
    message_error = ''
    usuariopk = request.POST["asistente"]
    especialidadpk = request.POST["especialidad"]
    user = User.objects.get(pk=usuariopk)
    group = Group.objects.get(pk=2)
    especialidad = Especialidad.objects.get(pk=especialidadpk)

    userGroup = list(User.groups.through.objects.filter(user_id=user.pk, group_id=group.pk))
    if len(userGroup) == 0:  # Verificamos si el usuario tiene el rol
        group.user_set.add(user)  # sino se le asigna el rol al usuario

    registro = Asistente.objects.filter(user_id=user.pk, especialidad_id=especialidadpk)
    if (registro.__len__() == 0):
        Asistente.objects.create(user=user, especialidad=especialidad)
    else:
        message_error = "El asistente ya se encuentra registrado"
    return JsonResponse({"message_error": message_error}, status=200)


def listarAsistentes(request):
    especialidadpk = request.POST["especialidad"]
    registros = Asistente.objects.filter(especialidad_id=especialidadpk)
    asistentes = []
    for item in registros:
        asistentes.append(item.user)
    ser_instance = serializers.serialize('json', asistentes)
    return JsonResponse({"asistentes": ser_instance}, status=200)


def eliminarAsistente(request):
    asistentepk = request.POST['asistentepk']
    especialidadpk = request.POST['especialidad']
    asistente = Asistente.objects.get(especialidad_id=especialidadpk, user_id=asistentepk)
    group = Group.objects.get(pk=2)  # asistente

    # Quitar rol de asistente de especialidad a usuario si es necesario
    usuario = User.objects.get(pk=asistentepk)
    registros = list(Asistente.objects.filter(user_id=asistentepk))
    if len(registros) == 1:
        group.user_set.remove(usuario)

    asistente.delete()
    return JsonResponse({}, status=200)
