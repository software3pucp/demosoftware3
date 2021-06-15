import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect

from django.core import serializers
from gestionarEspecialidad.models import Especialidad
from gestionarFacultad.models import Facultad
from gestionarREAcreditadoras.models import Acreditadora, ResultadoAcreditadora
from gestionarIndicadores.models import Indicador
from django.contrib.auth.decorators import login_required
# Create your views here.
from gestionarResultados.models import ResultadoPUCP

@login_required
def listarRE(request, pk):
    lista=[]
    acreditadora = Acreditadora.objects.get(pk=pk)
    resultados = ResultadoAcreditadora.objects.filter(acreditadora=pk)
    indicadores=Indicador.objects.all()
    if indicadores:
        for ind in indicadores:
            repucp=ResultadoPUCP.objects.get(pk=ind.resultado_id)
            id_especialidad = repucp.especialidad_id
            especialidad = Especialidad.objects.get(pk=id_especialidad)
            id_facultad = especialidad.facultad_id
            facultad = Facultad.objects.get(pk=id_facultad)
            reacres= ResultadoAcreditadora.objects.filter(acreditadora=pk, indicador_id=ind.pk)
            if reacres:
                reg=[repucp,especialidad,facultad,reacres]
                lista.append(reg)

    context = {
        'acreditadora': acreditadora,
        'resultados': resultados,
        'repucps' : lista,
    }
    return render(request, 'gestionarREAcreditadoras/listarRE.html', context)

@login_required
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
                                                                             indicador_id=request.POST["select"])

            pk = resultadoAcreditadora.pk
            insert = True
            flag = 2
            return redirect('listarRE', acreditadora.pk)

    if pk != '0':
        resultadoAcreditadora = ResultadoAcreditadora.objects.get(pk=pk)
        if resultadoAcreditadora.indicador_id:
            id_indicador=resultadoAcreditadora.indicador_id
            indi=Indicador.objects.get(pk=id_indicador)
            resultadoPUCP=ResultadoPUCP.objects.get(pk=indi.resultado_id)
            # resultadoSeleccionado = resultadoAcreditadora.resultadoPUCP_id
            especialidadSeleccionada = resultadoPUCP.especialidad_id
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
            ind_Aux=[];
            indicadores=Indicador.objects.filter(estado='1');
            for ind in indicadores:
                # print(ind.descripcion)
                result_aux=ResultadoPUCP.objects.get(pk=ind.resultado.pk)
                if result_aux.especialidad_id == int(request.POST['especialidadPk']):
                    resul_Acre_Aux=ResultadoAcreditadora.objects.filter(indicador_id=ind.pk)
                    if not resul_Acre_Aux:
                        ind_Aux.append(ind);

            data = serializers.serialize("json", ind_Aux)
            return JsonResponse({"resp": data}, status=200)
    return
