from django.contrib.auth.models import Group
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.core import serializers
from authentication.models import User
from gestionarEspecialidad.models import Especialidad, Auditor


@login_required
def auditores(request):
    especialidades = []
    if (request.user.rol_actual == "Coordinador de especialidad"):
        usuario = request.user
        grupo = Group.objects.get(name="Coordinador de especialidad")
        especialidades = Especialidad.objects.filter(responsable=usuario.pk)
    context = {
        'ListaUsuarios': User.objects.all(),
        'especialidades': especialidades,
    }
    return render(request, 'gestionarAuditores/auditores.html', context)


def registrarAuditor(request):
    message_error = ''
    usuariopk = request.POST["auditor"]
    especialidadpk = request.POST["especialidad"]
    user = User.objects.get(pk=usuariopk)
    group = Group.objects.get(pk=3)
    especialidad = Especialidad.objects.get(pk=especialidadpk)

    userGroup = list(User.groups.through.objects.filter(user_id=user.pk, group_id=group.pk))
    if len(userGroup) == 0:  # Verificamos si el usuario tiene el rol
        group.user_set.add(user)  # sino se le asigna el rol al usuario

    registro = Auditor.objects.filter(user_id=user.pk)
    if (registro.__len__() == 0):
        Auditor.objects.create(user=user, especialidad=especialidad)
    else:
        message_error = "El auditor ya se encuentra registrado"
    return JsonResponse({"message_error": message_error}, status=200)


def listarAuditores(request):
    especialidadpk = request.POST["especialidad"]
    registros = Auditor.objects.filter(especialidad_id=especialidadpk)
    auditores = []
    for item in registros:
        auditores.append(item.user)
    ser_instance = serializers.serialize('json', auditores)
    return JsonResponse({"auditores": ser_instance}, status=200)


def eliminarAuditor(request):
    usuariopk = request.POST['auditorpk']
    especialidadpk = request.POST['especialidad']
    auditor = Auditor.objects.get(especialidad_id=especialidadpk, user_id=usuariopk)
    group = Group.objects.get(pk=3)  # auditor

    # Quitar rol de auditor de especialidad a usuario si es necesario
    usuario = User.objects.get(pk=usuariopk)
    registros = list(Auditor.objects.filter(user_id=usuariopk))
    if len(registros) == 1:
        group.user_set.remove(usuario)

    auditor.delete()
    return JsonResponse({}, status=200)
