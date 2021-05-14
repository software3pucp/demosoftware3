import gestionarEspecialidad
from gestionarEspecialidad.models import Especialidad
from gestionarFacultad.models import Facultad
from gestionarCurso.models import Curso
from django.shortcuts import render, redirect
from authentication.models import User

# Create your views here.
from gestionarFacultad.views import listarFacultadxEsp, listarFacultad


def listarEspecialidad(request):
    context = {
        'ListaEspecialidad': Especialidad.objects.all(),
        'ListaFacultad': Facultad.objects.all(),
    }
    return render(request, 'gestionarEspecialidad/listarEspecialidad.html', context)


def listarEspecialidadxCurso(request, id_especialidad):
    print("==================================")
    print(id_especialidad)
    print("==================================")

    context = {
        'ListaCurso': Curso.objects.filter(especialidad_id=id_especialidad),
        'ListaEspecialidad': Especialidad.objects.all(),
        'id_especialidad': id_especialidad
    }
    return render(request, 'gestionarCurso/listarCurso.html', context)


def agregarEspecialidad(request, id_facultad):
    if request.POST:
        print(request.POST)
        nombre = request.POST['name']
        id_responsable = request.POST['responsable']
        foto = request.FILES['photo']
        facultad = Facultad.objects.get(pk=id_facultad)
        Especialidad.objects.create(nombre=nombre, responsable=id_responsable, facultad=facultad, foto=foto)
        return listarFacultadxEsp(request, id_facultad)

    context = {
        'ListaUsuarios': User.objects.all(),
        'ListaFacultad': Facultad.objects.all(),
        'id_facultad': id_facultad
    }
    return render(request, 'gestionarEspecialidad/agregarEspecialidad.html', context)


def editarEspecialidad(request, id_especialidad, id_facultad):
    especialidad = Especialidad.objects.get(pk=id_especialidad)
    if request.POST:
        nuevo_nombre = request.POST["nombre"]
        nuevo_responsable = request.POST["responsable"]
        nueva_foto = request.POST["foto"]

        especialidad.nombre = nuevo_nombre
        especialidad.responsable = nuevo_responsable
        especialidad.foto = nueva_foto
        especialidad.save()

        return editarEspecialidad(request, id_especialidad, id_facultad)

    context = {
        'especialidad': especialidad,
        'id_especialidad': id_especialidad,
        'id_facultad': id_facultad
    }
    return render(request, 'gestionarEspecialidad/editarEspecialidad.html', context)
