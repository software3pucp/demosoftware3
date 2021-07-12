from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
# Create your views here.
from gestionarEspecialidad.models import Asistente, Auditor, Especialidad
from django.contrib.auth.models import Group

from gestionarFacultad.models import Facultad
from gestionarSemestre.models import Semestre


@login_required
def reportes(request):
    especialidades = []
    facultades = []
    semestres = Semestre.objects.filter()

    if (request.user.rol_actual == "Asistente de acreditación"):
        usuario = request.user
        especialidades = []
        items = Asistente.objects.filter(user_id=usuario.pk)
        for item in items:
            especialidades.append(item.especialidad)
        context = {
            'semestres':semestres,
            'especialidades': especialidades,
        }
        return render(request, 'reportes/reportesCE.html', context)

    if (request.user.rol_actual == "Auditor"):
        usuario = request.user
        especialidades = []
        items = Auditor.objects.filter(user_id=usuario.pk)
        for item in items:
            especialidades.append(item.especialidad)
        context = {
            'semestres': semestres,
            'especialidades': especialidades,
        }
        return render(request, 'reportes/reportesCE.html', context)

    if (request.user.rol_actual == "Coordinador de facultad"):
        usuario = request.user
        grupo = Group.objects.get(pk=4)
        facultades = Facultad.objects.filter(responsable=usuario.pk)
        context = {
            'semestres': semestres,
            'facultades': facultades,
        }
        return render(request, 'reportes/reportesCF.html', context)

    if (request.user.rol_actual == "Coordinador de especialidad"):
        usuario = request.user
        grupo = Group.objects.get(pk=5)
        especialidades = Especialidad.objects.filter(responsable=usuario.pk)
        context = {
            'semestres': semestres,
            'especialidades': especialidades,
        }
        return render(request, 'reportes/reportesCE.html', context)

def obtenerEspecialidades(request):
    id_facultad = request.POST['facultad']
    especialidades = Especialidad.objects.filter(facultad_id=id_facultad, estado='1')
    data = serializers.serialize("json", especialidades)
    return JsonResponse({"resp": data}, status=200)