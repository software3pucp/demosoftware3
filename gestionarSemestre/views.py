from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.models import Group
# Create your views here.
from datetime import datetime

from gestionarEspecialidad.models import Especialidad
from gestionarFacultad.models import Facultad
from gestionarHorario.models import Horario
from gestionarPlanMedicion.models import PlanMedicionCurso, PlanMedicion
from gestionarSemestre.models import Semestre
from gestionarCurso.models import Curso
from django.contrib.auth.decorators import login_required


@login_required
def listarSemestre(request):
    semestreLista = Semestre.objects.filter().order_by("nombreCodigo")

    context = {
        'ListaSemestre': semestreLista
    }
    return render(request, 'gestionarSemestre/listarSemestre.html', context)


@login_required
def agregarSemestre(request):
    anho = int(request.POST["nombreCodigo"][0:4])
    etapa = int(request.POST["nombreCodigo"][5:6])
    meses = {
        "01": "Enero",
        "02": "Febrero",
        "03": "Marzo",
        "04": "Abril",
        "05": "Mayo",
        "06": "Junio",
        "07": "Julio",
        "08": "Agosto",
        "09": "Septiembre",
        "10": "Octubre",
        "11": "Noviembre",
        "12": "Diciembre",
    }

    fechaIni = request.POST["inicio"][0:2] + " de " + meses[request.POST["inicio"][3:5]]
    fechaFin = request.POST["fin"][0:2] + " de " + meses[request.POST["fin"][3:5]]
    semestre = Semestre.objects.create(nombreCodigo=request.POST["nombreCodigo"], anho=anho,
                                       etapa=etapa, inicio=fechaIni, fin=fechaFin)
    ser_instance = serializers.serialize('json', [semestre, ])
    return JsonResponse({"nuevoSemestre": ser_instance}, status=200)


@login_required
def enviarCursoHorario(request, pk):
    if request.POST:
        planMedicion = PlanMedicion.objects.filter(estado='1', especialidad_id=request.POST['especialidad']).filter(
            semestre=pk)
        try:
            listaCursos = []
            planMedicionCursos = PlanMedicionCurso.objects.filter(estado=1, semestre=pk,
                                                                  planMedicion=planMedicion[0].pk)
            for planMedicionCurso in planMedicionCursos:
                curso = Curso.objects.get(pk=planMedicionCurso.curso_id, especialidad_id=request.POST['especialidad'])
                print(curso.nombre)
                listaCursos.append(curso)
        except:
            print("No existe plan de medicion asociado!!!")

        for i in range(len(listaCursos)):
            print(listaCursos[i].nombre)
        ser_instance = serializers.serialize('json', listaCursos)
        return JsonResponse({"cursoLista": ser_instance}, status=200)

    semestre = Semestre.objects.get(pk=pk)

    if (request.user.rol_actual == "Asistente de acreditación"):
        usuario = request.user
        grupo = Group.objects.get(pk=2)
        especialidades = Especialidad.objects.filter(responsable=usuario.pk)
        context = {
            "semestreSeleccionado": semestre,
            'especialidades': especialidades,
        }
        return render(request, 'gestionarSemestre/semestre/semestreDetalleCE.html', context)

    if (request.user.rol_actual == "Auditor"):
        usuario = request.user
        grupo = Group.objects.get(pk=3)
        especialidades = Especialidad.objects.filter(responsable=usuario.pk)
        context = {
            "semestreSeleccionado": semestre,
            'especialidades': especialidades,
        }
        return render(request, 'gestionarSemestre/semestre/semestreDetalleCE.html', context)

    if (request.user.rol_actual == "Coordinador de facultad"):
        usuario = request.user
        grupo = Group.objects.get(pk=4)
        facultades = Facultad.objects.filter(responsable=usuario.pk)
        context = {
            "semestreSeleccionado": semestre,
            'facultades': facultades,
        }
        return render(request, 'gestionarSemestre/semestre/semestreDetalleCF.html', context)

    if (request.user.rol_actual == "Coordinador de especialidad"):
        usuario = request.user
        grupo = Group.objects.get(pk=5)
        especialidades = Especialidad.objects.filter(responsable=usuario.pk)
        context = {
            "semestreSeleccionado": semestre,
            'especialidades': especialidades,
        }
        return render(request, 'gestionarSemestre/semestre/semestreDetalleCE.html', context)



@login_required
def listarSemestreDocente(request):
    horarios_docente = Horario.objects.filter(responsable_id=request.user.pk)
    listaCursos = []
    listarSemestres = []
    for horario in horarios_docente:
        if (horario.curso.planMedicion.estado == '1'):
            listaCursos.append(horario.curso.curso)
            listarSemestres.append(horario.curso.semestre)

    listarSemestres = list(set(listarSemestres))

    context = {
        'ListaSemestre': listarSemestres
    }
    return render(request, 'gestionarSemestre/listarSemestreDocente.html', context)


@login_required
def enviarCursoHorarioDocente(request, semestrepk):
    listaCursos = []
    try:
        horarios_docente = Horario.objects.filter(responsable_id=request.user.pk)
        for horario in horarios_docente:
            if (horario.curso.planMedicion.estado == '1' and horario.curso.semestre.pk == int(semestrepk)):
                listaCursos.append(horario.curso.curso)
        listaCursos = list(set(listaCursos))
    except:
        print("No existe plan de medicion docente asociado!!!")
    print(listaCursos)
    semestre = Semestre.objects.get(pk=semestrepk)
    context = {
        "semestreSeleccionado": semestre,
        'listaCursos': listaCursos
    }
    return render(request, 'gestionarSemestre/semestre/semestreDetalleDocente.html', context)


def eliminarSemestre(request):
    semestrepk = int(request.POST['semestrepk'])
    semestre = Semestre.objects.get(pk=semestrepk)
    # evaluamos si se ha programado un plan de medicion en el semestre
    semestresxplan = PlanMedicion.semestre.through.objects.all()
    tieneMediciones = False
    for item in semestresxplan:
        itempk =item.semestre.pk
        if (itempk == semestrepk):
            tieneMediciones = True
            break
    if(not tieneMediciones): # se elimina si no hay mediciones en el semestre
        semestre.delete()
    return JsonResponse({"tieneMediciones":tieneMediciones}, status=200)
