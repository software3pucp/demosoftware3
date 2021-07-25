import gestionarEspecialidad
from gestionarEspecialidad.models import Especialidad
from demosoftware3.settings import MEDIA_URL
from gestionarEspecialidad.views import listarEspecialidadxCurso
from gestionarFacultad.models import Facultad
from gestionarCurso.models import Curso
from django.shortcuts import render, redirect
from authentication.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
from gestionarHorario.models import Horario

@login_required(login_url='login')
def listarCurso(request):
    context = {
        'ListaEspecialidad': Especialidad.objects.all(),
        'ListaCurso': Curso.objects.filter(estado=Curso.ESTADOS[1][0]),
        'ListaEstados': Curso.ESTADOS[1:],
        'estado': '1'
    }
    return render(request, 'gestionarCurso/listarCurso.html', context)

@login_required
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

@login_required
def agregarCurso(request, id_especialidad):
    media_path = MEDIA_URL
    if request.POST:
        if ('name' in request.POST):
            nombre = request.POST['name']
            especialidad = Especialidad.objects.get(pk=id_especialidad)
            Curso.objects.create(nombre=nombre, especialidad=especialidad,
                                 estado=request.POST['estado'])
            return redirect('listarEspecialidadxCurso',id_especialidad)


    context = {
            'ListaUsuarios': User.objects.all(),
            'ListaEspecialidad': Especialidad.objects.all(),
            'id_especialidad': id_especialidad,
            'media_path': media_path,
            'estado': request.POST["estado"]
        }
    return render(request, 'gestionarCurso/agregarCurso.html', context)

@login_required
def editarCurso(request, id_curso):
    curso = Curso.objects.get(pk=id_curso)
    id_especialidad = curso.especialidad_id
    estado = curso.estado
    media_path = MEDIA_URL
    if request.POST:
        nuevo_nombre = request.POST["name"]
        curso.nombre = nuevo_nombre
        curso.save()
        return redirect('listarEspecialidadxCurso', id_especialidad)

    context = {
        'curso': curso,
        'estado':estado
    }
    return render(request, 'gestionarCurso/editarCurso.html', context)

@login_required
def eliminarCurso(request, id_curso):
    curso = Curso.objects.get(pk=id_curso)
    espPK = curso.especialidad_id
    curso.delete()
    return redirect('listarEspecialidadxCurso', espPK)

@login_required
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
    return redirect('listarEspecialidadxCurso',id_especialidad)
