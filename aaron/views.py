from django.shortcuts import render, redirect
import requests
from django.shortcuts import render

# Create your views here.
from aaron.models import Waffles


# Create your views here.


def aaronHome(request):
    wafflesList = Waffles.objects.filter()

    if request.POST:

        if request.POST["tipoform"] == "1":
            Waffles.objects.create(name=request.POST["name"], precio=request.POST["precio"])

        context = {
            'titulo': "Has guardado en BBDD :" + request.POST["name"],
            'listaWaffles': wafflesList,
        }

        return render(request, 'aaron/listaWaffles.html', context)

    context = {
        'titulo': 'HE ENTRADO POR URL',
        'listaWaffles': wafflesList,
    }

    return render(request, 'aaron/home.html', context)


# Create your views here.
def listaWaffles(request):
    wafflesList = Waffles.objects.filter()
    context = {
        'titulo': 'Lista de Waffles',
        'listaWaffles': wafflesList,
    }

    return render(request, 'aaron/listaWaffles.html', context)


def detalleWaffles(request, pk):
    waffle = Waffles.objects.get(pk=pk)

    print(waffle)

    context = {
        'waffle': waffle
    }
    return render(request, 'aaron/detalle.html', context)


def editarWaffles(request, pk):
    waffle = Waffles.objects.get(pk=pk)
    if request.POST:
        print(request.POST)
        newname = request.POST["name"]
        newprecio = request.POST["precio"]

        waffle.name = newname
        waffle.precio = newprecio
        waffle.save()

        return redirect(listaWaffles)

    context = {
        'waffle': waffle
    }
    return render(request, 'aaron/editar.html', context)
def eliminarWaffles(request,pk):

    waffle = Waffles.objects.get(pk=pk)
    waffle.delete()
    return redirect(listaWaffles)

