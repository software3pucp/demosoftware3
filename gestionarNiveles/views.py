from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core import serializers

from gestionarEspecialidad.models import Especialidad
from gestionarFacultad.models import Facultad
from gestionarNiveles.models import Nivel

def editarNivel(request,pk):
     if request.POST:
         pk=request.POST['nivelpk']
         nivel = Nivel.objects.get(pk=pk)
         nivel.nombre = request.POST['nombre']
         nivel.valor = request.POST['valor']
         nivel.save()
         return redirect('niveles')

     nivel = Nivel.objects.get(pk=pk)
     context = {
         'nivel': nivel,
     }
     return render(request, 'gestionarNiveles/editarNivel.html', context)

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

def listarNiveles(request):
    id_especialidad = request.POST['especialidadpk']
    niveles = Nivel.objects.filter(especialidad_id=id_especialidad, estado='1').order_by('valor')
    ser_instance = serializers.serialize('json', niveles)
    return JsonResponse({"niveles": ser_instance}, status=200)

def eliminarNivel(request):
    id_nivel = request.POST['nivelpk']
    nivel = Nivel.objects.get(pk=id_nivel)
    nivel.estado = '0'  # eliminación lógica
    nivel.save()
    return JsonResponse({}, status=200)

def crearNivel(request):

    id_especialidad= request.POST['especialidadpk']

    print(id_especialidad)
    try:
        especialidad = Especialidad.objects.get(pk=id_especialidad)
    except:
        print("Error al buscar la especialidad")

    nombre = request.POST['nombreNivel']
    valor = request.POST['valorNivel']
    nivel = Nivel.objects.create(nombre=nombre, valor=valor, especialidad=especialidad)
    ser_instance = serializers.serialize('json', [nivel, ])
    return JsonResponse({"nuevoNivel": ser_instance}, status=200)