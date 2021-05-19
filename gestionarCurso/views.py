import gestionarEspecialidad
from gestionarEspecialidad.models import Especialidad
from demosoftware3.settings import MEDIA_URL
from gestionarEspecialidad.views import listarEspecialidadxCurso
from gestionarFacultad.models import Facultad
from gestionarCurso.models import Curso
from django.shortcuts import render, redirect
from authentication.models import User

# Create your views here.
from gestionarHorario.models import Horario


def listarCurso(request):
    context = {
        'ListaEspecialidad': Especialidad.objects.all(),
        'ListaCurso': Curso.objects.all(),
    }
    return render(request, 'gestionarCurso/listarCurso.html', context)


def listarCursoxHorario(request, id_curso):
    print("==================================")
    print(id_curso)
    print("==================================")
    media_path = MEDIA_URL
    context = {
        'ListaHorario': Horario.objects.filter(curso_id=id_curso),
        'ListaCurso': Curso.objects.all(),
        'id_curso': id_curso,
        'media_path': media_path
    }
    return render(request, 'gestionarHorario/listarHorario.html', context)


def agregarCurso(request, id_especialidad):
    if request.POST:
        print(request.POST)
        nombre = request.POST['name']
        id_responsable = request.POST['responsable']
        especialidad = Especialidad.objects.get(pk=id_especialidad)
        Curso.objects.create(nombre=nombre, responsable=id_responsable, especialidad=especialidad)
        return redirect('listarEspecialidadxCurso', id_especialidad)

    context = {
        'ListaUsuarios': User.objects.all(),
        'ListaEspecialidad': Especialidad.objects.all(),
        'id_especialidad': id_especialidad
    }
    return render(request, 'gestionarCurso/agregarCurso.html', context)


def editarCurso(request, id_curso):
    curso = Curso.objects.get(pk=id_curso)
    if request.POST:
        nuevo_nombre = request.POST["name"]
        nuevo_responsable = request.POST["responsable"]
        curso.codigo = nuevo_nombre
        curso.responsable = nuevo_responsable
        curso.save()
        return redirect('listarEspecialidadxCurso', curso.especialidad_id)

    context = {
        'curso': curso,
        'ListaUsuarios': User.objects.all()
    }
    return render(request, 'gestionarCurso/editarCurso.html', context)


def eliminarCurso(request, id_curso):
    curso = Curso.objects.get(pk=id_curso)
    espPK = curso.especialidad_id
    curso.delete()
    return redirect('listarEspecialidadxCurso', espPK)
