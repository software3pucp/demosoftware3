from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core import serializers

from gestionarEspecialidad.models import Especialidad
from gestionarFacultad.models import Facultad
from gestionarNiveles.models import Nivel

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
     return render(request, 'gestionarNiveles/editarNiv.html', context)

def niveles(request):

    facultades = Facultad.objects.filter(estado='1')

    context = {
        'facultades':facultades,
    }
    return render(request, 'gestionarNiveles/niveles.html', context)


def obtenerEspecialidades(request):
    id_facultad = request.POST['facultadpk']
    especialidades = Especialidad.objects.filter(facultad_id=id_facultad, estado='1')
    data = serializers.serialize("json", especialidades)
    return JsonResponse({"resp": data}, status=200)

def crearNivel(request):

    print('----------------------------------------------------')
    print(request.POST)
    print('-----------------------------------------------------')

    id_especialidad= request.POST['especialidadpk']
    try:
        especialidad = Especialidad.objects.get(pk=id_especialidad)
    except:
        print("Error al buscar la especialidad")

    nombre = request.POST['name']
    valor = request.POST['value']
    nivel = Nivel.objects.create(name=nombre, value=valor, especialidad=especialidad)
    ser_instance = serializers.serialize('json', [nivel, ])
    return JsonResponse({"nuevoNivel": ser_instance}, status=200)