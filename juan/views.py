from django.shortcuts import render

# Create your views here.

from juan.models import Characters

def juanHome(request):
    if request.POST:
        Characters.objects.create(name=request.POST["nombre"],type=request.POST["tipo"],
                                  gender=request.POST["sexo"],weapon=request.POST["arma"])
        context = {
            'guardado': "Se ha guardado el personaje "+request.POST["nombre"],
        }
    else:
        context = {
            'guardado': "Nada ",
        }
    return render(request, 'juan/home.html', context)

def listar(request):
    chList = Characters.objects.filter()
    context = {
        'listaPersonajes': chList
    }
    return render(request, 'juan/listado.html', context)
