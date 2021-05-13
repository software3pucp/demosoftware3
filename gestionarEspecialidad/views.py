from gestionarEspecialidad.models import Especialidad
from django.shortcuts import render,redirect
from demosoftware3.settings import MEDIA_URL
# Create your views here.
def listarEspecialidad(request):
    media_path = MEDIA_URL
    context = {
        'media_path':media_path,
        'ListaEspecialidad': Especialidad.objects.all()
    }
    return render(request, 'gestionarEspecialidad/listarEspecialidad.html', context)

def agregarEspecialidad(request):
    if request.POST:
        nombre = request.POST['name']
        id_responsable = request.POST['responsable']
        foto = request.FILES['photo']
        Especialidad.objects.create(nombre=nombre, responsable=id_responsable, foto=foto)
        return redirect(listarEspecialidad)
    context = {

    }
    return render(request, 'gestionarEspecialidad/agregarEspecialidad.html', context)
