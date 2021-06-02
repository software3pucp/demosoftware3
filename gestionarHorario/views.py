import gestionarEspecialidad
from gestionarEspecialidad.models import Especialidad
from gestionarEspecialidad.views import listarEspecialidadxCurso
from gestionarFacultad.models import Facultad
from gestionarCurso.models import Curso
from gestionarHorario.models import Horario
from django.shortcuts import render, redirect
from authentication.models import User


# Create your views here.
def listarHorario(request):
    context = {
        'ListaCurso': Curso.objects.all(),
        'ListaHorario': Horario.objects.all(),
        'ListaEstados': Horario.ESTADOS[1:],
    }
    return render(request, 'gestionarHorario/listarHorario.html', context)


def agregarHorario(request, id_curso):
    if request.POST:
        print(request.POST)
        codigo = request.POST['name']
        id_responsable = request.POST['responsable']
        curso = Curso.objects.get(pk=id_curso)
        Horario.objects.create(codigo=codigo, responsable=id_responsable, curso=curso, estado=Horario.ESTADOS[1][0])
        return redirect('listarCursoxHorario', id_curso)

    context = {
        'ListaUsuarios': User.objects.all(),
        'ListaCurso': Curso.objects.all(),
        'id_curso': id_curso
    }
    return render(request, 'gestionarHorario/agregarHorario.html', context)


def editarHorario(request, id_horario):
    horario = Horario.objects.get(pk=id_horario)
    if request.POST:
        nuevo_nombre = request.POST["name"]
        nuevo_responsable = request.POST["responsable"]
        horario.codigo = nuevo_nombre
        horario.responsable = nuevo_responsable
        horario.save()
        return redirect('listarCursoxHorario', horario.curso_id)

    context = {
        'horario': horario,
        'ListaUsuarios': User.objects.all(),
        'id_responsable': horario.responsable,
    }
    return render(request, 'gestionarHorario/editarHorario.html', context)


def eliminarHorario(request, id_horario):
    horario = Horario.objects.get(pk=id_horario)
    cursoPK = horario.curso_id
    horario.delete()
    return redirect('listarCursoxHorario', cursoPK)


def eliminarHorario2(request, id_horario):
    horario = Horario.objects.get(pk=id_horario)
    cursoPK = horario.curso_id
    horario.estado = Horario.ESTADOS[2][0]
    horario.save()
    return redirect('listarCursoxHorario', cursoPK)
