import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect

from django.core import serializers
from gestionarEspecialidad.models import Especialidad
from gestionarFacultad.models import Facultad
from gestionarREAcreditadoras.models import Acreditadora, ResultadoAcreditadora, HistoriaREAcred
from gestionarIndicadores.models import Indicador
from django.contrib.auth.decorators import login_required
# Create your views here.
from gestionarResultados.models import ResultadoPUCP
from itertools import chain

from gestionarResultados.models import PlanResultados


@login_required
def listarRE(request, pk):
    try:
        lista = []
        acreditadora = Acreditadora.objects.get(pk=pk)
        resultados = ResultadoAcreditadora.objects.filter(acreditadora=pk,estado=1)
        plResPucp=PlanResultados.objects.filter(estado=1)
        if plResPucp:
            for plan in plResPucp:
                listaAux=[]
                auxfac=None
                auxesp=None
                resultadosPUCPs=ResultadoPUCP.objects.filter(estado=1,planResultado_id=plan.pk)
                for rPUCP in resultadosPUCPs:
                    indic = Indicador.objects.filter(resultado_id=rPUCP.pk, estado=1)
                    pksREA = []
                    for ind in indic:
                        if ind.resultadoAcreditadora_id:
                            pksREA.append(ind.resultadoAcreditadora_id)
                    # print(pksREA)
                    id_especialidad = plan.especialidad_id
                    especialidad = Especialidad.objects.get(pk=id_especialidad)
                    id_facultad = especialidad.facultad_id
                    facultad = Facultad.objects.get(pk=id_facultad)
                    auxfac = facultad
                    auxesp = especialidad
                    reacres = ResultadoAcreditadora.objects.filter(pk__in=pksREA, estado=1)
                    if reacres:
                        reg = [rPUCP, reacres]
                        # print(reg)
                        listaAux.append(reg)
                if auxfac is not None:
                    if listaAux:
                        reg = [listaAux, auxesp, auxfac]
                        lista.append(reg)
        print("DEBUG")
        print(lista)
        for i in lista:
            for a in i[0]:
                print(a[0].descripcion)
                print("================================")
                for zzz in a[1]:
                    print(zzz.descripcion)
                print("================================")

        context = {
            'acreditadora': acreditadora,
            'resultados': resultados,
            'repucps' : lista,
        }
        return render(request, 'gestionarREAcreditadoras/listarRE.html', context)
    except:
        return JsonResponse({"resp": None}, status=303)


def conectarIndicadores(listaIndicadores,pk):
    print(listaIndicadores)
    print(pk)
    if listaIndicadores:
        indicadoresVincular=Indicador.objects.filter(pk__in=listaIndicadores,estado=1)
        if indicadoresVincular:
            for i in indicadoresVincular:
                i.resultadoAcreditadora_id=pk
                i.save()
    indicadoresDesvincular=Indicador.objects.filter(resultadoAcreditadora_id=pk, estado=1).exclude(pk__in=listaIndicadores)
    if indicadoresDesvincular:
        for i in indicadoresDesvincular:
            i.resultadoAcreditadora = None
            i.save()


@login_required
def editarRE(request, pk):
    # try:
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
        indicadoresAsociados = []
        iAUX = Indicador.objects.filter(resultadoAcreditadora_id=pk, estado=1)
        if iAUX:
            for i in iAUX:
                indicadoresAsociados.append(i.pk)
        else:
            indicadoresAsociados = []

        listaIndicadoresMarcados = []
        for key, values in request.POST.lists():
            # print(key, values)
            if key == 'select':
                listaIndicadoresMarcados=values

        if request.POST:
            # print(request.POST)
            if request.POST['operacion'] == 'entrada':
                resultadoAcreditadora.acreditadora_id = request.POST["acreditadora"]

            elif request.POST['operacion'] == 'editar':
                resultadoAcreditadora = ResultadoAcreditadora.objects.get(pk=pk)
                resultadoAcreditadora.codigo = request.POST["codigo"]
                resultadoAcreditadora.descripcion = request.POST["descripcion"]
                conectarIndicadores(listaIndicadoresMarcados,pk)
                resultadoAcreditadora.acreditadora_id = request.POST["acreditadora"]
                resultadoAcreditadora.save()
                flag = 1
                return redirect('listarRE', acreditadora.pk)

            elif request.POST['operacion'] == 'insertar':
                resultadoAcreditadora = ResultadoAcreditadora.objects.create(codigo=request.POST["codigo"],
                                                                                 descripcion=request.POST["descripcion"],
                                                                                 acreditadora_id=request.POST[
                                                                                     "acreditadora"])
                if ('select' in request.POST):
                    conectarIndicadores(listaIndicadoresMarcados,resultadoAcreditadora.pk)
                pk = resultadoAcreditadora.pk
                insert = True
                flag = 2
                return redirect('listarRE', acreditadora.pk)

        if pk != '0':
            resultadoAcreditadora = ResultadoAcreditadora.objects.get(pk=pk)
            planActivos = PlanResultados.objects.filter(estado=1)
            for plan in planActivos:
                resPucpAux = ResultadoPUCP.objects.filter(planResultado_id=plan.pk, estado=1);
                for resP in resPucpAux:
                    indi = Indicador.objects.filter(resultado_id=resP.pk, resultadoAcreditadora_id=pk, estado=1)
                    if indi:
                        especialidadSeleccionada = plan.especialidad_id
                        facultadSeleccionada = Especialidad.objects.get(pk=especialidadSeleccionada).facultad_id

            titulo = 'Editar'
        else:
            titulo = 'Nuevo'

        context = {
            'insert': insert,
            'indicadorSeleccionado':id_indicador,
            'indicadoresAsociados': indicadoresAsociados,
            'resultadoAcreditadora': resultadoAcreditadora,
            'facultadSeleccionada': facultadSeleccionada,
            'especialidadSeleccionada': especialidadSeleccionada,
            'facultades': facultades,
            'flag': flag,
            'acreditadora': acreditadora,
            'titulo': titulo,
        }
        return render(request, 'gestionarREAcreditadoras/editarRE.html', context)
    # except:
    #     return JsonResponse({"resp": None}, status=303)

@login_required
def eliminarRE(request, pk):
    # Candidate.objects.filter(pk=pk).delete()
    print(request.POST)
    return

@login_required
def ajaxEditar(request):
    try:
        if request.POST:
            if request.POST['operacion'] == 'listEspe':
                especialidades = Especialidad.objects.filter(facultad_id=request.POST['facultad'], estado='1')
                data = serializers.serialize("json", especialidades)
                return JsonResponse({"resp": data}, status=200)
            if request.POST['operacion'] == 'listREPUCP':
                indicadores=[]
                planes = PlanResultados.objects.filter(especialidad_id=int(request.POST['especialidadPk']), estado=1)
                for p in planes:
                    res = ResultadoPUCP.objects.filter(planResultado_id=p.pk, estado=1)
                    for r in res:
                        auxInd = Indicador.objects.filter(resultado_id=r.pk, resultadoAcreditadora_id=None, estado=1)
                        for i in auxInd:
                            indicadores.append(i)
                        auxInd2 = Indicador.objects.filter(resultado_id=r.pk, resultadoAcreditadora_id=int(
                            request.POST['resultadoAcredPK']), estado=1)
                        for x in auxInd2:
                            indicadores.append(x)
                data = serializers.serialize("json", indicadores)
                return JsonResponse({"resp": data}, status=200)
    except:
        return JsonResponse({"resp": None}, status=303)
    return

@login_required
def activarREA(request):
    try:
        re=ResultadoAcreditadora.objects.get(pk=request.POST["reAcreditadoraPK"])
        re.estado = '1'
        re.save()
        return JsonResponse({}, status=200)
    except:
        return JsonResponse({"resp": None}, status=303)

@login_required
def desactivarREA(request):
    try:
        re=ResultadoAcreditadora.objects.get(pk=request.POST["reAcreditadoraPK"])
        re.estado = '2'
        re.save()
        indic=Indicador.objects.filter(resultadoAcreditadora_id=request.POST["reAcreditadoraPK"], estado=1)
        for i in indic:
            print(i.codigo, i.descripcion)
            # resAux=ResultadoPUCP.objects.get(pk=i.resultado_id)
            # plRAux=PlanResultados.objects.get(pk=resAux.planResultado_id)
            # espAux=Especialidad.objects.get(pk=plRAux.especialidad_id)
            # facAux=Facultad.objects.get(pk=espAux.facultad_id)
            # HistoriaREAcred.objects.create(resultadoAcreditadora_id=request.POST["reAcreditadoraPK"],
            #                                 codIndicador=i.codigo, descpIndicador=i.descripcion,
            #                                 facultad=facAux.nombre,
            #                                 especialidad=espAux.nombre)
            i.resultadoAcreditadora=None
            i.save()
        return JsonResponse({}, status=200)
    except:
        return JsonResponse({"resp": None}, status=303)

@login_required
def listarREA(request):
    try:
        id_acreditadora = request.POST['acreditadora']
        reAcre = ResultadoAcreditadora.objects.filter(acreditadora_id=id_acreditadora).exclude(estado=0)
        ser_instance = serializers.serialize('json', reAcre)
        return JsonResponse({"reAcre": ser_instance}, status=200)
    except:
        return JsonResponse({"resp": None}, status=303)