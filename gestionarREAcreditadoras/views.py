import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect

from django.core import serializers
from gestionarEspecialidad.models import Especialidad
from gestionarFacultad.models import Facultad
from gestionarREAcreditadoras.models import Acreditadora, ResultadoAcreditadora
from gestionarIndicadores.models import Indicador

# Create your views here.
from gestionarResultados.models import ResultadoPUCP


def listarRE(request, pk):
    lista=[]
    acreditadora = Acreditadora.objects.get(pk=pk)
    resultados = ResultadoAcreditadora.objects.filter(acreditadora=pk)
    repucps=ResultadoPUCP.objects.all()
    if repucps:
        for repucp in repucps:
            id_especialidad = repucp.especialidad_id
            especialidad = Especialidad.objects.get(pk=id_especialidad)
            id_facultad = especialidad.facultad_id
            facultad = Facultad.objects.get(pk=id_facultad)
            reacres= ResultadoAcreditadora.objects.filter(acreditadora=pk, resultadoPUCP_id=repucp.pk)
            if reacres:
                reg=[repucp,especialidad,facultad,reacres]
                lista.append(reg)

    context = {
        'acreditadora': acreditadora,
        'resultados': resultados,
        'repucps' : lista,
    }
    return render(request, 'gestionarREAcreditadoras/listarRE.html', context)


def editarRE(request, pk):
    insert = False
    flag = 0
    resultadoSeleccionado = 0
    especialidadSeleccionada = 0
    facultadSeleccionada = 0
    resultadoAcreditadora = ResultadoAcreditadora()
    resultadoAcreditadora.pk = pk
    acreditadora = Acreditadora.objects.get(pk=request.POST["acreditadora"])
    facultades = Facultad.objects.filter(estado='1')
    if request.POST:
        # print(request.POST)
        if request.POST['operacion'] == 'entrada':
            resultadoAcreditadora.acreditadora_id = request.POST["acreditadora"]
            # print('***************************************************************************************************')
            # print(request.POST)
            # print('***************************************************************************************************')

        elif request.POST['operacion'] == 'editar':
            resultadoAcreditadora = ResultadoAcreditadora.objects.get(pk=pk)
            resultadoAcreditadora.codigo = request.POST["codigo"]
            resultadoAcreditadora.descripcion = request.POST["descripcion"]
            if ('select' in request.POST):
                resultadoAcreditadora.resultadoPUCP_id = request.POST["select"]
            resultadoAcreditadora.acreditadora_id = request.POST["acreditadora"]
            resultadoAcreditadora.save()
            flag = 1
            return redirect('listarRE', acreditadora.pk)

        elif request.POST['operacion'] == 'insertar':
            if not ('select' in request.POST):
                resultadoAcreditadora = ResultadoAcreditadora.objects.create(codigo=request.POST["codigo"],
                                                                             descripcion=request.POST["descripcion"],
                                                                             acreditadora_id=request.POST[
                                                                                 "acreditadora"])
            else:
                resultadoAcreditadora = ResultadoAcreditadora.objects.create(codigo=request.POST["codigo"],
                                                                             descripcion=request.POST["descripcion"],
                                                                             acreditadora_id=request.POST[
                                                                                 "acreditadora"],
                                                                             resultadoPUCP_id=request.POST["select"])

            pk = resultadoAcreditadora.pk
            insert = True
            flag = 2
            return redirect('listarRE', acreditadora.pk)

    if pk != '0':
        resultadoAcreditadora = ResultadoAcreditadora.objects.get(pk=pk)
        if resultadoAcreditadora.resultadoPUCP_id is not None :
            resultadoSeleccionado = resultadoAcreditadora.resultadoPUCP_id
            especialidadSeleccionada = ResultadoPUCP.objects.get(pk=resultadoSeleccionado).especialidad_id
            facultadSeleccionada = Especialidad.objects.get(pk=especialidadSeleccionada).facultad_id

        titulo = 'Editar'
    else:
        titulo = 'Nuevo'

    context = {
        'insert': insert,
        'resultadoSeleccionado': resultadoSeleccionado,
        'resultadoAcreditadora': resultadoAcreditadora,
        'facultadSeleccionada': facultadSeleccionada,
        'especialidadSeleccionada': especialidadSeleccionada,
        'facultades': facultades,
        'flag': flag,
        'acreditadora': acreditadora,
        'titulo': titulo,
    }
    return render(request, 'gestionarREAcreditadoras/editarRE.html', context)


def eliminarRE(request, pk):
    # Candidate.objects.filter(pk=pk).delete()
    print(request.POST)
    return


def ajaxEditar(request):
    if request.POST:
        if request.POST['operacion'] == 'listEspe':
            especialidades = Especialidad.objects.filter(facultad_id=request.POST['facultad'], estado='1')
            data = serializers.serialize("json", especialidades)
            return JsonResponse({"resp": data}, status=200)
        if request.POST['operacion'] == 'listREPUCP':
            resultadosPUCP = ResultadoPUCP.objects.filter(especialidad_id=request.POST['especialidadPk'], estado='1');
            data = serializers.serialize("json", resultadosPUCP)
            return JsonResponse({"resp": data}, status=200)
    return
