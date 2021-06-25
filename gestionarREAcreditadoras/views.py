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
from itertools import chain

from gestionarResultados.models import PlanResultados


@login_required
def listarRE(request, pk):
    lista=[]
    acreditadora = Acreditadora.objects.get(pk=pk)
    resultados = ResultadoAcreditadora.objects.filter(acreditadora=pk,estado=1)
    plResPucp=PlanResultados.objects.filter(estado=1)
    impresionxFacultades=[]
    idFacultad=-1
    if plResPucp:
        for plan in plResPucp:
            resultadosPUCPs=ResultadoPUCP.objects.filter(estado=1,planResultado_id=plan.pk)
            for rPUCP in resultadosPUCPs:
                indic = Indicador.objects.filter(resultado_id=rPUCP.pk, estado=1)
                id_especialidad=plan.especialidad_id
                especialidad = Especialidad.objects.get(pk=id_especialidad)
                id_facultad = especialidad.facultad_id
                facultad = Facultad.objects.get(pk=id_facultad)
                reacres = []
                for i in indic:
                    reAux = ResultadoAcreditadora.objects.filter(indicador_id=i.pk, estado=1)
                    if reAux:
                        reacres = list(chain(reacres, reAux))
                        # print(reacres)
                if reacres:
                    reg = [rPUCP, especialidad, facultad, reacres]
                    # print(reg)
                    lista.append(reg)

    tabla_contenido = []
    for reg in lista:
        if reg==-1:
            idFacultad=reg[1].pk
        print(reg[1].pk)
        if idFacultad!=int(reg[1].pk):
            impresionxFacultades.append(tabla_contenido)
            tabla_contenido.clear()
            tabla_contenido.append(reg);
            idFacultad=reg[1].pk
        else:
            tabla_contenido.append(reg);
    print(impresionxFacultades)

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
    id_indicador = 0
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
                resultadoAcreditadora.indicador_id = request.POST["select"]
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
            planResultado=PlanResultados.objects.get(pk=resultadoPUCP.planResultado_id)
            # resultadoSeleccionado = planResultado.resultadoPUCP_id
            especialidadSeleccionada = planResultado.especialidad_id
            facultadSeleccionada = Especialidad.objects.get(pk=especialidadSeleccionada).facultad_id

        titulo = 'Editar'
    else:
        titulo = 'Nuevo'

    context = {
        'insert': insert,
        'indicadorSeleccionado':id_indicador,
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
                result_aux=ResultadoPUCP.objects.get(pk=ind.resultado.pk, estado=1)
                if result_aux:
                    # print(result_aux.descripcion)
                    plan=PlanResultados.objects.get(pk=result_aux.planResultado.pk,estado=1)
                    if plan.especialidad_id == int(request.POST['especialidadPk']):
                        resul_Acre_Aux=ResultadoAcreditadora.objects.filter(indicador_id=ind.pk, estado=1)
                        # print(request.POST['resultadoAcredPK'])
                        if not resul_Acre_Aux:
                           ind_Aux.append(ind);
                        else:
                           for reAcre in resul_Acre_Aux:
                              # print(reAcre.pk)
                              if int(request.POST['resultadoAcredPK'])!=0 and int(request.POST['resultadoAcredPK'])==reAcre.pk:
                                 ind_Aux.append(ind);
                                 break;

            data = serializers.serialize("json", ind_Aux)
            return JsonResponse({"resp": data}, status=200)
    return
