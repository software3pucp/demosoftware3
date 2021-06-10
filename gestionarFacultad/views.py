from demosoftware3.settings import MEDIA_URL
from gestionarFacultad.models import Facultad
from django.shortcuts import render, redirect
from authentication.models import User

from gestionarEspecialidad.models import Especialidad
from gestionarFacultad.models import Facultad
from django.shortcuts import render, redirect
from authentication.models import User


# Create your views here.
def listarFacultad(request):
    media_path = MEDIA_URL
    context = {
        'ListaFacultad': Facultad.objects.filter(estado=Facultad.ESTADOS[1][0]),
        'ListaFacultadInactivos': Facultad.objects.filter(estado=Facultad.ESTADOS[2][0]),
        'ListaEstados': Facultad.ESTADOS[1:],
        'media_path': media_path,
        'estado': '1'
    }
    return render(request, 'gestionarFacultad/listarFacultad.html', context)


def agregarFacultad(request):
    media_path = MEDIA_URL
    if request.POST:
        if ('name' in request.POST):
            nombre = request.POST['name']
            id_responsable = request.POST['responsable']
            foto = request.FILES['photo']
            Facultad.objects.create(nombre=nombre, responsable=id_responsable, foto=foto, estado=request.POST["estado"])
            context = {
                'ListaFacultad': Facultad.objects.filter(estado=Facultad.ESTADOS[1][0]),
                'ListaFacultadInactivos': Facultad.objects.filter(estado=Facultad.ESTADOS[2][0]),
                'ListaEstados': Facultad.ESTADOS[1:],
                'media_path': media_path,
                'estado':request.POST["estado"]
            }
            return render(request, 'gestionarFacultad/listarFacultad.html', context)
        else:
            context = {
                'ListaUsuarios': User.objects.all(),
                'estado':request.POST['estado'],
            }
            return render(request, 'gestionarFacultad/agregarFacultad.html', context)
    context = {
        'ListaUsuarios': User.objects.all(),
    }
    return render(request, 'gestionarFacultad/agregarFacultad.html', context)


def listarFacultadxEsp(request, id_facultad):
    media_path = MEDIA_URL
    context = {
        'ListaEspecialidad': Especialidad.objects.filter(facultad_id=id_facultad, estado=Facultad.ESTADOS[1][0]),
        'ListaEspecialidadInactivos': Especialidad.objects.filter(facultad_id=id_facultad, estado=Facultad.ESTADOS[2][0]),
        'ListaFacultad': Facultad.objects.all(),
        'id_facultad': id_facultad,
        'media_path': media_path,
        'ListaEstados': Especialidad.ESTADOS[1:],
        'estado': '1'
    }
    return render(request, 'gestionarEspecialidad/listarEspecialidad.html', context)


def editarFacultad(request, id_facultad):
    ListaUsuarios = User.objects.filter()
    media_path = MEDIA_URL
    facultad = Facultad.objects.get(pk=id_facultad)
    if request.POST:
        nuevo_nombre = request.POST["name"]
        nuevo_responsable = request.POST["responsable"]
        if request.FILES.get('photo'):
            nueva_foto = request.FILES["photo"]
            facultad.foto = nueva_foto
        facultad.nombre = nuevo_nombre
        facultad.responsable = nuevo_responsable
        context = {
            'ListaFacultad': Facultad.objects.filter(estado=Facultad.ESTADOS[1][0]),
            'ListaFacultadInactivos': Facultad.objects.filter(estado=Facultad.ESTADOS[2][0]),
            'ListaEstados': Facultad.ESTADOS[1:],
            'media_path': media_path,
            'estado': facultad.estado,
        }
        facultad.save()
        return render(request, 'gestionarFacultad/listarFacultad.html', context)

    context = {
        'facultad': facultad,
        'media_path': media_path,
        'ListaUsuarios': ListaUsuarios,
        'id_responsable': facultad.responsable,
    }
    return render(request, 'gestionarFacultad/editarFacultad.html', context)


def eliminarFacultad(request, id_facultad):
    media_path = MEDIA_URL
    facultad = Facultad.objects.get(pk=id_facultad)
    context = {
        'ListaFacultad': Facultad.objects.filter(estado=Facultad.ESTADOS[1][0]),
        'ListaFacultadInactivos': Facultad.objects.filter(estado=Facultad.ESTADOS[2][0]),
        'ListaEstados': Facultad.ESTADOS[1:],
        'media_path': media_path,
        'estado': facultad.estado,
    }
    facultad.delete()
    print("Correcto eliminar Facultad!")
    return render(request, 'gestionarFacultad/listarFacultad.html', context)


def eliminarFacultad2(request, id_facultad):
    media_path = MEDIA_URL
    facultad = Facultad.objects.get(pk=id_facultad)
    context = {
        'ListaFacultad': Facultad.objects.filter(estado=Facultad.ESTADOS[1][0]),
        'ListaFacultadInactivos': Facultad.objects.filter(estado=Facultad.ESTADOS[2][0]),
        'ListaEstados': Facultad.ESTADOS[1:],
        'media_path': media_path,
        'estado': facultad.estado,
    }
    if facultad.estado == Facultad.ESTADOS[2][0]:
        facultad.estado = Facultad.ESTADOS[1][0]
    elif facultad.estado == Facultad.ESTADOS[1][0]:
        facultad.estado = Facultad.ESTADOS[2][0]
    facultad.save()
    print("Correcto desactivar Facultad!")
    return render(request, 'gestionarFacultad/listarFacultad.html', context)
