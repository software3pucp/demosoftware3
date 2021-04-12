from django.shortcuts import render
# Create your views here.
import requests
from django.shortcuts import render
from jherson.models import Tipo, Pokemon
# Create your views here.


def jhersonHome(request):
    pokemons = Pokemon.objects.filter()
    context={
        'lPokemon': pokemons
    }
    return render(request,'jherson/home.html',context)

def jhersonInsertarPokemon(request):
    print("==============================================")
    print(request.POST)
    print("==============================================")
    ingresado = False
    if request.POST:
        Pokemon.objects.create(nombre=request.POST['nombre'], tipo_id=request.POST['tipo'],
                               altura=request.POST['altura'], peso=request.POST['peso'],
                               imagen=request.POST['link-imagen'])
        ingresado = True
    #Body
    tipos = Tipo.objects.filter()
    context={
        'lTipo' : tipos,
        'ingresado': ingresado,
    }
    return render(request,'jherson/insertarPokemon.html',context)