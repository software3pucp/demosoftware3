import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core import serializers
# Create your views here.
from gestionarEspecialidad.models import Especialidad
from gestionarIndicadores.models import Indicador
from gestionarNivel.models import Nivel
from gestionarResultados.models import ResultadoPUCP
from gestionarRubrica.models import Rubrica


def editarIndicador(request, pk):
    editado = False
    haydesc = False

    indicador = Indicador.objects.get(pk=pk)
    id_resultado = indicador.resultado_id
    nivelLista = Nivel.objects.filter(state=1)
    rubrica = Rubrica.objects.filter(indicador_id=pk)
    print(rubrica)
    nivelLista2 =[]
    for nivel in nivelLista:
        print(nivel.pk)
        for rub in rubrica:
            desc_nivel = ''
            print("rub ----------")
            print("rub:" + str(rub.nivel_id))
            if nivel.pk == rub.nivel_id:
                desc_nivel= rub.descripcion
        registro = [nivel,desc_nivel]
        nivelLista2.append(registro)

    print(nivelLista2)

    if len(rubrica)>0:
        haydesc=True

    if request.POST:
        indicador = Indicador.objects.get(pk=pk)
        indicador.codigo = request.POST['codigo']
        indicador.descripcion = request.POST['descripcion']
        indicador.save()
        editado = True
        context = {
            'indicador': indicador,
            'editado': editado,
            'id_resultado': id_resultado,
            'nivelLista': nivelLista,
            'rubrica':rubrica,
            'haydesc':haydesc,
            'desc_nivel':desc_nivel,
        }
        return render(request, 'gestionarIndicadores/editarIndicador.html', context)

    context = {
        'rubrica':rubrica,
        'haydesc':haydesc,
        'indicador': indicador,
        'editado': editado,
        'id_resultado': id_resultado,
        'nivelLista': nivelLista,
        'desc_nivel': desc_nivel,
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
        indicador.estado = 0
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
    esp = Especialidad.objects.get(pk=1)  # por ahora solo para una especialidad (Infomatica)
    niv = Nivel.objects.get(pk=request.POST['nivelpk'])
    ind = Indicador.objects.get(pk=request.POST['indicadorpk'])
    desc = request.POST['desc_nivel']
    desc_nivel = Rubrica.objects.create(especialidad=esp, nivel=niv, indicador=ind, descripcion=desc)
    ser_instance = serializers.serialize('json', [desc_nivel, ])
    return JsonResponse({"nuevaDesc_nivel": ser_instance}, status=200)