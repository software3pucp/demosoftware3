from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core import serializers

from gestionarNivel.models import Nivel


# def listarNiv(request):
#     flag =  False
#     if request.POST:
#         nivel = Nivel.objects.get(pk=request.POST['nivelPk'])
#         nivel.state=0
#         nivel.save()
#         flag = True
#
#     niveles= Nivel.objects.filter(state=1)
#     context = {
#         'nivelesList' : niveles,
#         'flag' : flag
#     }
#     return render(request, 'gestionarNivel/listarNiv.html', context)
#
# def crearNiv(request):
#     registrado = False
#     if request.POST:
#         Nivel.objects.create(name=request.POST['name'], value=request.POST['value'])
#         registrado = True
#     context = {
#         'registrado': registrado,
#     }
#     return render(request, 'gestionarNivel/crearNiv.html', context)
#
def editarNiv(request,pk):

     if request.POST:
         nivel = Nivel.objects.get(pk=pk)
         nivel.name = request.POST['name']
         nivel.value = request.POST['value']
         nivel.save()
         return redirect('listarNivel')

     nivel = Nivel.objects.get(pk=pk)
     context = {
         'nivel': nivel,
     }
     return render(request, 'gestionarNivel/editarNiv.html', context)

def listarNivel(request):
    flag = False
    if request.POST:
             nivel = Nivel.objects.get(pk=request.POST['nivelPk'])
             nivel.state=0
             nivel.save()
             flag = True
    nivelLista = Nivel.objects.filter(state=1)
    context = {
       'nivelLista': nivelLista,
        'flag': flag
    }
    return render(request,'gestionarNivel/listarNivel.html', context)

def agregarNivel(request):
    nombre = request.POST['name']
    valor = request.POST['value']
    nivel = Nivel.objects.create(name=nombre, value=valor)
    ser_instance = serializers.serialize('json', [nivel, ])
    return JsonResponse({"nuevoNivel": ser_instance}, status=200)