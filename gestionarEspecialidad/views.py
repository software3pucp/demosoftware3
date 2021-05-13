from gestionarEspecialidad.models import Especialidad
from django.shortcuts import render,redirect

# Create your views here.
def listarEspecialidad(request):
    context = {
        'ListaEspecialidad': Especialidad.objects.all(),
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
