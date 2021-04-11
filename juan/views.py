from django.shortcuts import render

# Create your views here.

from juan.models import Characters

def juanHome(request):
    if request.POST:
        Characters.objects.create(name=request.POST["nombre"],type=request.POST["tipo"],
                                  gender=request.POST["sexo"],weapon=request.POST["arma"],
                                  image=request.POST["imagen"])
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

def personajeDetalle(request,pk):
    personaje = Characters.objects.get(pk=pk)

    context = {
        "personajeDetalle": personaje
    }
    return render(request, 'juan/personajes/personajeDetalle.html', context)

def actualizar(request,pk):
    if request.POST:
        print(request.POST)
        personaje = Characters.objects.get(pk=pk)
        personaje.name = request.POST["nombre"]
        personaje.type = request.POST["elemento"]
        personaje.gender = request.POST["sexo"]
        personaje.weapon = request.POST["arma"]
        personaje.save()

    else:
        personaje = Characters.objects.get(pk=pk)

    lPersonajes = Characters.objects.filter()
    context = {
        "listaPersonajes": lPersonajes
    }

    return render(request, 'juan/listado.html', context)

def eliminar(request,pk):
    if request.POST:
        personaje = Characters.objects.get(pk=pk)
        personaje.delete()
    else:
        personaje = Characters.objects.get(pk=pk)

    lPersonajes = Characters.objects.filter()
    context = {
        "listaPersonajes": lPersonajes
    }

    return render(request, 'juan/listado.html', context)