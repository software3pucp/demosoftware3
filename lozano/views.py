import requests
from django.shortcuts import render

from lozano.models import Tipo, Pokemon


def lozanoHome(request):
    print('*************************************************')
    print(request.POST)
    print('*************************************************')

    flag = False
    if request.POST:
        pokemon = Pokemon.objects.get(pk = request.POST['pokemonPk'])
        pokemon.estado = 0
        pokemon.save()
        flag = True
    pokemons = Pokemon.objects.filter(estado=1)
    context = {
        'lPokemon' : pokemons,
        'flag' : flag,
    }
    return render(request, 'lozano/home.html', context)


def lozanoInsertarPokemon(request):
    print('*************************************************')
    print(request.POST)
    print('*************************************************')

    flag = False
    if request.POST:
        Pokemon.objects.create(nombre=request.POST['nombre'],tipo_id=request.POST['tipo'],altura=request.POST['altura'],peso=request.POST['peso'],imagen=request.POST['link-imagen'])
        flag = True

    #Body
    tipos = Tipo.objects.filter()
    context = {
        'lTipo' : tipos,
        'flag' : flag,
    }
    return render(request, 'lozano/insertarPokemon.html', context)

def lozanoEditarPokemon(request, pk):
    print('*************************************************')
    print(request.POST)
    print('*************************************************')

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
    return render(request, 'lozano/editarPokemon.html', context)

def lozanoPokemonDetalle(request, pk):
    pokemon = Pokemon.objects.get(pk=pk)

    context = {
        'pokemon' : pokemon,
    }
    return render(request, 'lozano/pokemonDetalle.html', context)