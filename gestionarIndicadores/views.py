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
from django.contrib.auth.decorators import login_required


@login_required
def editarIndicador(request, pk):
    indicador = Indicador.objects.get(pk=pk)
    especialidadpk = obtenerEspecialidadIndicador(indicador)
    planPk = obtenerPlanResultados(indicador)
    id_resultado = indicador.resultado_id
    nivelLista = Nivel.objects.filter(estado='1', especialidad_id=especialidadpk,plaResultado_id=planPk).order_by('valor')
    rubrica = Rubrica.objects.filter(indicador_id=pk)
    nivelLista2 = []
    hay_niveles = False
    mensaje_aviso = ''
    if (len(nivelLista) > 0):
        hay_niveles = True
    else:
        mensaje_aviso = "Aun no se han registrado niveles de desempeño en la +\
                     especialidad! Por favor registar niveles de desempeño"

    for nivel in nivelLista:  # Creamos una lista de registros- registo (nivel, descripcion)
        registro = [nivel, '']  # incialmente la descripción esta vacía
        nivelLista2.append(registro)

    for nivel in nivelLista:
        for rub in rubrica:  # se verifica en la rúbrica si ya existen descripciones para un determinado nivel
            if nivel.pk == rub.nivel_id:
                desc_nivel = rub.descripcion
                nivelLista2[nivel.valor - 1][1] = desc_nivel

    if request.POST:
        indicador = Indicador.objects.get(pk=pk)
        indicador.codigo = request.POST['codigo']
        indicador.descripcion = request.POST['descripcion']
        indicador.save()
        for nivel in nivelLista:  # se agrega las descripciones por cada nivel
            desc = request.POST['desc_nivel' + str(nivel.pk)]
            agregarDescipcionNivel(indicador.pk, nivel.pk, desc)
        context = {
            'indicador': indicador,
            'id_resultado': id_resultado,
            'nivelLista': nivelLista2,
            'rubrica': rubrica,
            'hay_niveles': hay_niveles,
            'mensaje_aviso': mensaje_aviso,
        }
        return redirect('editarResultado', pk=id_resultado)

    context = {
        'rubrica': rubrica,
        'indicador': indicador,
        'id_resultado': id_resultado,
        'nivelLista': nivelLista2,
        'hay_niveles': hay_niveles,
        'mensaje_aviso': mensaje_aviso,
    }
    return render(request, 'gestionarIndicadores/editarIndicador.html', context)


def obtenerEspecialidadIndicador(indicador):
    id_resultado = indicador.resultado_id;
    resultado = ResultadoPUCP.objects.get(pk=id_resultado)
    especialidad = resultado.planResultado.especialidad
    return especialidad.pk

def obtenerPlanResultados(indicador):
    id_resultado = indicador.resultado_id;
    resultado = ResultadoPUCP.objects.get(pk=id_resultado)
    return resultado.planResultado_id



@login_required
def eliminarIndicadorxResultado(request):
    indicadorpk = request.POST['indicadorpk']
    indicador = Indicador.objects.get(pk=indicadorpk)
    indicador.estado = 0  # eliminación lógica
    indicador.save()
    return JsonResponse({}, status=200)


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
        indicador = Indicador.objects.get(pk=indicardorpk)
        resultado = ResultadoPUCP.objects.get(pk=indicador.resultado_id)
        esp = resultado.planResultado.especialidad
        niv = Nivel.objects.get(pk=nivelpk)
        ind = Indicador.objects.get(pk=indicardorpk)
        Rubrica.objects.create(especialidad=esp, nivel=niv, indicador=ind, descripcion=desc)

