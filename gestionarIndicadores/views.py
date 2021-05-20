import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core import serializers
# Create your views here.
from rest_framework.utils import json
from gestionarEspecialidad.models import Especialidad
from gestionarIndicadores.models import Indicador
from gestionarNivel.models import Nivel
from gestionarResultados.models import ResultadoPUCP
from gestionarRubrica.models import Rubrica


def editarIndicador(request, pk):
    editado = False
    guardado = False
    indicador = Indicador.objects.get(pk=pk)
    id_resultado = indicador.resultado_id
    nivelLista = Nivel.objects.filter(state=1).order_by('value')
    rubrica = Rubrica.objects.filter(indicador_id=pk)
    nivelLista2 =[]

    for nivel in nivelLista:
        registro=[nivel,'']
        nivelLista2.append(registro)

    for nivel in nivelLista:
        for rub in rubrica:
            if nivel.pk == rub.nivel_id:
                desc_nivel= rub.descripcion
                nivelLista2[nivel.value-1][1]=desc_nivel
    nivelLista=nivelLista2

    if request.POST:
        indicador = Indicador.objects.get(pk=pk)
        indicador.codigo = request.POST['codigo']
        indicador.descripcion = request.POST['descripcion']
        indicador.save()
        editado = True
        guardado = True
        context = {
            'indicador': indicador,
            'editado': editado,
            'id_resultado': id_resultado,
            'nivelLista': nivelLista,
            'rubrica':rubrica,
            'guardado' : guardado
        }
        return render(request, 'gestionarIndicadores/editarIndicador.html', context)

    context = {
        'rubrica':rubrica,
        'indicador': indicador,
        'editado': editado,
        'id_resultado': id_resultado,
        'nivelLista': nivelLista,
    }
    return render(request, 'gestionarIndicadores/editarIndicador.html', context)

def listarIndicadorxResultado(request, id_resultado):

    listaIndicadores = Indicador.objects.filter(estado=1, resultado_id=id_resultado)
    context = {
        'listaIndicadores': listaIndicadores,
        'resultado': ResultadoPUCP.objects.get(pk=id_resultado)
    }
    return render(request, 'gestionarIndicadores/listarIndicadorxResultado.html', context)


def eliminarIndicadorxResultado(request, id_resultado):
    if request.POST:
        print(request.POST)
        indicador = Indicador.objects.get(pk=request.POST['indicador_pk'])
        indicador.estado = 0 #eliminación lógica
        indicador.save()
        flag = True
        return redirect('editarResultado', pk=id_resultado)
    return redirect('home')


def agregarIndicador(request, id_resultado):
    codigo = request.POST['codigoI']
    descripcion = request.POST['descripcionI']
    resultado = ResultadoPUCP.objects.get(pk=id_resultado)
    indicador = Indicador.objects.create(codigo=codigo, descripcion=descripcion, resultado=resultado)
    ser_instance = serializers.serialize('json', [indicador, ])
    return JsonResponse({"nuevoIndicador": ser_instance}, status=200)

def agregarDescipcionNivel(request):
    try:
        desc_nivel = Rubrica.objects.get(indicador_id=request.POST['indicadorpk'], nivel_id=request.POST['nivelpk'])
        desc_nivel.descripcion = request.POST['desc_nivel']
        desc_nivel.save()
    except:
        esp = Especialidad.objects.get(pk=1)  # por ahora solo para una especialidad (Infomatica)
        niv = Nivel.objects.get(pk=request.POST['nivelpk'])
        ind = Indicador.objects.get(pk=request.POST['indicadorpk'])
        desc = request.POST['desc_nivel']
        desc_nivel = Rubrica.objects.create(especialidad=esp, nivel=niv, indicador=ind, descripcion=desc)
        #print('se registró')
    ser_instance = serializers.serialize('json', [desc_nivel, ])
    return JsonResponse({"nuevaDesc_nivel": ser_instance}, status=200)