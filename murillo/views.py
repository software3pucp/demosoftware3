import requests
from django.shortcuts import render

# Create your views here.
from murillo.models import Tipo, Pokemon


def murilloHome(request):
    print('*************************************************')
    print(request.POST)
    print('*************************************************')

    flag = False
    if request.POST:
        pokemon = Pokemon.objects.get(pk=request.POST['pokemonPk'])
        pokemon.estado = 0
        pokemon.save()
        flag = True
    pokemons = Pokemon.objects.filter(estado=1)
    context = {
        'lPokemon': pokemons,
        'flag': flag,
    }
    return render(request, 'murillo/home.html', context)


def murilloInsertarPokemon(request):
    print('*******************************')
    print(request.POST)
    print('*******************************')

    ingresado = False
    if request.POST:
        Pokemon.objects.create(nombre=request.POST['nombre'],tipo_id=request.POST['tipo'],altura=request.POST['altura'],peso=request.POST['peso'],imagen=request.POST['link-imagen'])
        ingresado = True
    #Body
    tipos = Tipo.objects.filter()
    context = {
        'lTipo' : tipos,
        'ingresado' : ingresado,
    }
    return render(request, 'murillo/insertar-pokemon.html', context)


def murilloPokemonDetalle(request, pk):

    pokemon = Pokemon.objects.get(pk=pk)

    context = {
        'pokemon' : pokemon,
    }
    return render(request,'murillo/detalle-pokemon.html',context)

def murilloPokemonEditar(request,pk):
    print('*******************************')
    print(request.POST)
    print('*******************************')

    flag = False
    if request.POST:
        pokemon = Pokemon.objects.get(pk=pk)
        pokemon.nombre = request.POST['nombre']
        pokemon.tipo_id = request.POST['tipo']
        pokemon.altura = request.POST['altura']
        pokemon.peso = request.POST['peso']
        pokemon.imagen = request.POST['link-imagen']
        pokemon.save()
        flag = True
    pokemon = Pokemon.objects.get(pk=pk)
    tipos = Tipo.objects.filter()
    context = {
        'pokemon' : pokemon,
        'lTipo': tipos,
        'flag': flag,
    }
    return render(request, 'murillo/editar-pokemon.html', context)