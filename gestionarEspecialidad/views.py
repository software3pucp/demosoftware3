import gestionarEspecialidad
from demosoftware3.settings import MEDIA_URL
from gestionarEspecialidad.models import Especialidad
from gestionarFacultad.models import Facultad
from gestionarCurso.models import Curso
from django.shortcuts import render, redirect
from authentication.models import User

# Create your views here.
from gestionarFacultad.views import listarFacultadxEsp, listarFacultad


def listarEspecialidad(request):
    media_path = MEDIA_URL
    context = {
        'ListaEspecialidad': Especialidad.objects.all(),
        'ListaFacultad': Facultad.objects.all(),
        'media_path': media_path
    }
    return render(request, 'gestionarEspecialidad/listarEspecialidad.html', context)


def listarEspecialidadxCurso(request, id_especialidad):
    print("==================================")
    print(id_especialidad)
    print("==================================")
    media_path = MEDIA_URL
    context = {
        'ListaCurso': Curso.objects.filter(especialidad_id=id_especialidad),
        'ListaEspecialidad': Especialidad.objects.all(),
        'id_especialidad': id_especialidad,
        'id_facultad': Especialidad.objects.get(pk=id_especialidad).facultad.pk,
        'media_path': media_path
    }
    return render(request, 'gestionarCurso/listarCurso.html', context)


def agregarEspecialidad(request, id_facultad):
    media_path = MEDIA_URL
    if request.POST:
        print(request.POST)
        nombre = request.POST['name']
        id_responsable = request.POST['responsable']
        foto = request.FILES['photo']
        facultad = Facultad.objects.get(pk=id_facultad)
        Especialidad.objects.create(nombre=nombre, responsable=id_responsable, facultad=facultad, foto=foto)
        return redirect('listarFacultadxEsp', id_facultad)

    context = {
        'ListaUsuarios': User.objects.all(),
        'ListaFacultad': Facultad.objects.all(),
        'id_facultad': id_facultad,
        'media_path': media_path
    }
    return render(request, 'gestionarEspecialidad/agregarEspecialidad.html', context)


def editarEspecialidad(request, id_especialidad):
    especialidad = Especialidad.objects.get(pk=id_especialidad)
    if request.POST:
        print(request.POST)
        nuevo_nombre = request.POST["name"]
        nuevo_responsable = request.POST["responsable"]
        nueva_foto = request.FILES["photo"]

        especialidad.nombre = nuevo_nombre
        especialidad.responsable = nuevo_responsable
        especialidad.foto = nueva_foto
        especialidad.save()
        return redirect('listarFacultadxEsp', especialidad.facultad.pk)

    context = {
        'especialidad': especialidad,
        'ListaUsuarios': User.objects.all()
    }
    return render(request, 'gestionarEspecialidad/editarEspecialidad.html', context)


def eliminarEspecialidad(request, id_especialidad):
    especialidad = Especialidad.objects.get(pk=id_especialidad)
    fakuPK = especialidad.facultad.pk
    especialidad.delete()
    return redirect('listarFacultadxEsp', fakuPK)
