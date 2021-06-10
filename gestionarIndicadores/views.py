import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core import serializers
# Create your views here.
from rest_framework.utils import json
from gestionarEspecialidad.models import Especialidad
from gestionarIndicadores.models import Indicador
from gestionarNiveles.models import Nivel
from gestionarResultados.models import ResultadoPUCP
from gestionarRubrica.models import Rubrica


def editarIndicador(request, pk):
    indicador = Indicador.objects.get(pk=pk)
    id_resultado = indicador.resultado_id
    nivelLista = Nivel.objects.filter(state=1).order_by('value')
    rubrica = Rubrica.objects.filter(indicador_id=pk)
    nivelLista2 =[]
    hay_niveles = False
    if (len(nivelLista)>0):
        hay_niveles = True

    for nivel in nivelLista: # Creamos una lista de registros- registo (nivel, descripcion)
        registro=[nivel,''] # incialmente la descripción esta vacía
        nivelLista2.append(registro)

    for nivel in nivelLista:
        for rub in rubrica: # se verifica en la rúbrica si ya existen descripciones para un determinado nivel
            if nivel.pk == rub.nivel_id:
                desc_nivel = rub.descripcion
                nivelLista2[nivel.value-1][1] = desc_nivel

    if request.POST:
        indicador = Indicador.objects.get(pk=pk)
        indicador.codigo = request.POST['codigo']
        indicador.descripcion = request.POST['descripcion']
        indicador.save()
        for nivel in nivelLista: # se agrega las descripciones por cada nivel
            desc = request.POST['desc_nivel'+ str(nivel.pk)]
            agregarDescipcionNivel(indicador.pk, nivel.pk, desc)

        context = {
            'indicador': indicador,
            'id_resultado': id_resultado,
            'nivelLista': nivelLista2,
            'rubrica':rubrica,
            'hay_niveles': hay_niveles,
        }
        return redirect('editarResultado', pk=id_resultado)

    context = {
        'rubrica':rubrica,
        'indicador': indicador,
        'id_resultado': id_resultado,
        'nivelLista': nivelLista2,
        'hay_niveles': hay_niveles,
    }
    return render(request, 'gestionarIndicadores/editarIndicador.html', context)


def eliminarIndicadorxResultado(request, id_resultado):
    if request.POST:
        print(request.POST)
        indicador = Indicador.objects.get(pk=request.POST['indicador_pk'])
        indicador.estado = 0 #eliminación lógica
        indicador.save()
        return redirect('editarResultado', pk=id_resultado)


def agregarIndicador(request, id_resultado):
    codigo = request.POST['codigoI']
    descripcion = request.POST['descripcionI']
    resultado = ResultadoPUCP.objects.get(pk=id_resultado)
    indicador = Indicador.objects.create(codigo=codigo, descripcion=descripcion, resultado=resultado)
    ser_instance = serializers.serialize('json', [indicador, ])
    return JsonResponse({"nuevoIndicador": ser_instance}, status=200)

def agregarDescipcionNivel(indicardorpk, nivelpk, desc):
    try:
        desc_nivel = Rubrica.objects.get(indicador_id=indicardorpk, nivel_id=nivelpk)
        desc_nivel.descripcion = desc
        desc_nivel.save()
    except:
        esp = Especialidad.objects.get(pk=1)  # por ahora solo para una especialidad (Infomatica)
        niv = Nivel.objects.get(pk=nivelpk)
        ind = Indicador.objects.get(pk=indicardorpk)
        Rubrica.objects.create(especialidad=esp, nivel=niv, indicador=ind, descripcion=desc)