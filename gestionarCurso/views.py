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
        'ListaCurso': Curso.objects.filter(estado=Curso.ESTADOS[1][0]),
        'ListaEstados': Curso.ESTADOS[1:],
        'estado': '1'
    }
    return render(request, 'gestionarCurso/listarCurso.html', context)


def listarCursoxHorario(request, id_curso):
    media_path = MEDIA_URL
    context = {
        'ListaHorario': Horario.objects.filter(curso_id=id_curso, estado=Horario.ESTADOS[1][0]),
        'ListaHorarioInactivos': Horario.objects.filter(curso_id=id_curso, estado=Horario.ESTADOS[2][0]),
        'ListaCurso': Curso.objects.all(),
        'id_curso': id_curso,
        'id_especialidad': Curso.objects.get(pk=id_curso).especialidad.pk,
        'media_path': media_path,
        'ListaEstados': Curso.ESTADOS[1:],
        'estado': '1'
    }
    return render(request, 'gestionarHorario/listarHorario.html', context)


def agregarCurso(request, id_especialidad):
    media_path = MEDIA_URL
    if request.POST:
        if ('name' in request.POST):
            nombre = request.POST['name']
            id_responsable = request.POST['responsable']
            especialidad = Especialidad.objects.get(pk=id_especialidad)
            Curso.objects.create(nombre=nombre, responsable=id_responsable, especialidad=especialidad,
                                 estado=request.POST['estado'])
            context = {
                'ListaCurso': Curso.objects.filter(especialidad_id=id_especialidad, estado=Especialidad.ESTADOS[1][0]),
                'ListaCursoInactivos': Curso.objects.filter(especialidad_id=id_especialidad,
                                                            estado=Especialidad.ESTADOS[2][0]),
                'ListaEspecialidad': Especialidad.objects.all(),
                'id_especialidad': id_especialidad,
                'id_facultad': Especialidad.objects.get(pk=id_especialidad).facultad.pk,
                'media_path': media_path,
                'ListaEstados': Especialidad.ESTADOS[1:],
                'estado': request.POST['estado']
            }
            return render(request, 'gestionarCurso/listarCurso.html', context)


    context = {
            'ListaUsuarios': User.objects.all(),
            'ListaEspecialidad': Especialidad.objects.all(),
            'id_especialidad': id_especialidad,
            'media_path': media_path,
            'estado': request.POST["estado"]
        }
    return render(request, 'gestionarCurso/agregarCurso.html', context)


def editarCurso(request, id_curso):
    curso = Curso.objects.get(pk=id_curso)
    id_especialidad = curso.especialidad_id
    estado = curso.estado
    media_path = MEDIA_URL
    if request.POST:
        nuevo_nombre = request.POST["name"]
        nuevo_responsable = request.POST["responsable"]
        curso.nombre = nuevo_nombre
        curso.responsable = nuevo_responsable
        curso.save()
        context = {
            'ListaCurso': Curso.objects.filter(especialidad_id=id_especialidad, estado=Especialidad.ESTADOS[1][0]),
            'ListaCursoInactivos': Curso.objects.filter(especialidad_id=id_especialidad,
                                                        estado=Especialidad.ESTADOS[2][0]),
            'ListaEspecialidad': Especialidad.objects.all(),
            'id_especialidad': id_especialidad,
            'id_facultad': Especialidad.objects.get(pk=id_especialidad).facultad.pk,
            'media_path': media_path,
            'ListaEstados': Especialidad.ESTADOS[1:],
            'estado': estado
        }
        return render(request, 'gestionarCurso/listarCurso.html', context)

    context = {
        'curso': curso,
        'ListaUsuarios': User.objects.all(),
        'id_responsable': curso.responsable,
        'estado':estado
    }
    return render(request, 'gestionarCurso/editarCurso.html', context)


def eliminarCurso(request, id_curso):
    curso = Curso.objects.get(pk=id_curso)
    espPK = curso.especialidad_id
    curso.delete()
    return redirect('listarEspecialidadxCurso', espPK)


def eliminarCurso2(request, id_curso):
    curso = Curso.objects.get(pk=id_curso)
    estado = curso.estado
    media_path = MEDIA_URL
    id_especialidad = curso.especialidad_id
    if curso.estado == Curso.ESTADOS[2][0]:
        curso.estado = Curso.ESTADOS[1][0]
    elif curso.estado == Curso.ESTADOS[1][0]:
        curso.estado = Curso.ESTADOS[2][0]
    curso.save()
    context = {
        'ListaCurso': Curso.objects.filter(especialidad_id=id_especialidad, estado=Especialidad.ESTADOS[1][0]),
        'ListaCursoInactivos': Curso.objects.filter(especialidad_id=id_especialidad,
                                                    estado=Especialidad.ESTADOS[2][0]),
        'ListaEspecialidad': Especialidad.objects.all(),
        'id_especialidad': id_especialidad,
        'id_facultad': Especialidad.objects.get(pk=id_especialidad).facultad.pk,
        'media_path': media_path,
        'ListaEstados': Especialidad.ESTADOS[1:],
        'estado': estado
    }
    return render(request, 'gestionarCurso/listarCurso.html', context)
