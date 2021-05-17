import gestionarEspecialidad
from gestionarEspecialidad.models import Especialidad
from gestionarEspecialidad.views import listarEspecialidadxCurso
from gestionarFacultad.models import Facultad
from gestionarCurso.models import Curso
from django.shortcuts import render, redirect
from authentication.models import User


# Create your views here.
def listarCurso(request):
    context = {
        'ListaEspecialidad': Especialidad.objects.all(),
        'ListaCurso': Curso.objects.all(),
    }
    return render(request, 'gestionarCurso/listarCurso.html', context)


def agregarCurso(request, id_especialidad):
    if request.POST:
        print(request.POST)
        nombre = request.POST['name']
        id_responsable = request.POST['responsable']
        especialidad = Especialidad.objects.get(pk=id_especialidad)
        Curso.objects.create(nombre=nombre, responsable=id_responsable, especialidad=especialidad)
        return listarEspecialidadxCurso(request, id_especialidad)

    context = {
        'ListaUsuarios': User.objects.all(),
        'ListaEspecialidad': Especialidad.objects.all(),
        'id_especialidad': id_especialidad
    }
    return render(request, 'gestionarCUrso/agregarCurso.html', context)


def editarCurso(request, id_curso):
    curso = Curso.objects.get(pk=id_curso)
    if request.POST:
        nuevo_nombre = request.POST["name"]
        nuevo_responsable = request.POST["responsable"]
        curso.nombre = nuevo_nombre
        curso.responsable = nuevo_responsable
        curso.save()

        return listarEspecialidadxCurso(request, curso.especialidad_id)

    context = {
        'curso': curso,
        'ListaUsuarios': User.objects.all()
    }
    return render(request, 'gestionarCurso/editarCurso.html', context)


def eliminarCurso(request, id_curso):
    curso = Curso.objects.get(pk=id_curso)
    espPK = curso.especialidad_id
    curso.delete()
    return listarEspecialidadxCurso(request, espPK)
