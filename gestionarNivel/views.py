from django.shortcuts import render, redirect

from gestionarNivel.models import Nivel


def listarNiv(request):
    flag =  False
    if request.POST:
        nivel = Nivel.objects.get(pk=request.POST['nivelPk'])
        nivel.state=0
        nivel.save()
        flag = True

    niveles= Nivel.objects.filter(state=1)
    context = {
        'nivelesList' : niveles,
        'flag' : flag
    }
    return render(request, 'gestionarNivel/listarNiv.html', context)

def crearNiv(request):
    registrado = False
    if request.POST:
        Nivel.objects.create(name=request.POST['name'], value=request.POST['value'])
        registrado = True
    context = {
        'registrado': registrado,
    }
    return render(request, 'gestionarNivel/crearNiv.html', context)

def editarNiv(request,pk):
    flag = False
    if request.POST:
        nivel = Nivel.objects.get(pk=pk)
        nivel.name = request.POST['name']
        nivel.value = request.POST['value']
        nivel.save()
        flag = True
    nivel = Nivel.objects.get(pk=pk)
    context = {
        'nivel': nivel,
        'flag': flag,
    }
    return render(request, 'gestionarNivel/editarNiv.html', context)
