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
        'ListaFacultad': Facultad.objects.all(),
        'media_path': media_path
    }
    return render(request, 'gestionarFacultad/listarFacultad.html', context)


def crearFacultad(request):
    if request.POST:
        nombre = request.POST['name']
        id_responsable = request.POST['responsable']
        foto = request.FILES['photo']
        Facultad.objects.create(nombre=nombre, responsable=id_responsable, foto=foto)
        return redirect(listarFacultad)
    context = {
        'ListaUsuarios': User.objects.all(),
    }
    return render(request, 'gestionarFacultad/crearFacultad.html', context)


def listarFacultadxEsp(request, id_facultad):
    media_path = MEDIA_URL
    print("==================================")
    print(id_facultad)
    print("==================================")

    context = {
        'ListaEspecialidad': Especialidad.objects.filter(facultad_id=id_facultad),
        'ListaFacultad': Facultad.objects.all(),
        'id_facultad': id_facultad,
        'media_path': media_path
    }
    return render(request, 'gestionarEspecialidad/listarEspecialidad.html', context)
