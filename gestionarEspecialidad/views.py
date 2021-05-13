from gestionarEspecialidad.models import Especialidad
from gestionarFacultad.models import Facultad
from django.shortcuts import render,redirect
from authentication.models import User

# Create your views here.
def listarEspecialidad(request):
    context = {
        'ListaEspecialidad': Especialidad.objects.all(),
        'ListaFacultad': Facultad.objects.all(),
    }
    return render(request, 'gestionarEspecialidad/listarEspecialidad.html', context)

def agregarEspecialidad(request):
    if request.POST:
        nombre = request.POST['name']
        id_responsable = request.POST['responsable']
        foto = request.FILES['photo']
        facultad = request.POST['facultadPK']
        Especialidad.objects.create(nombre=nombre, responsable=id_responsable, facultad=facultad, foto=foto)
        return redirect(listarEspecialidad)
    context = {
        'ListaUsuarios': User.objects.all(),
        'ListaFacultad': Facultad.objects.all(),
    }
    return render(request, 'gestionarEspecialidad/agregarEspecialidad.html', context)

