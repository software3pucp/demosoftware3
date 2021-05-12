import requests
from django.shortcuts import render

from gestionarRE.models import Acreditadora,ResultadoAcreditadora, Resultado


# Create your views here.


def listarRE(request):
    resultados = ResultadoAcreditadora.objects.filter(acreditadora=1)
    context = {
        'resultados' : resultados,
    }
    return render(request,'gestionarRE/listarRE.html',context)


def editarRE(request,pk):
    insert = False
    flag = 0
    resultadoAcreditadora = ResultadoAcreditadora()
    resultadoAcreditadora.pk = pk
    resultadosSelec = []
    resultados = Resultado.objects.filter()

    if request.POST:
        if request.POST['operacion'] == 'entrada':
            resultadoAcreditadora.acreditadora_id = request.POST["acreditadora"]

        elif request.POST['operacion'] == 'editar':
            resultadoAcreditadora = ResultadoAcreditadora.objects.get(pk=pk)
            resultadosSelec = Resultado.objects.filter(resultadosAcreditadora=pk)
            resultadoAcreditadora.codigo = request.POST['codigo']
            resultadoAcreditadora.descripcion = request.POST['descripcion']
            resultadoAcreditadora.save()

            for i in resultados:
                id = 'select' + str(i.pk)
                if request.POST[id] == '1' and i not in resultadosSelec:
                    i.resultadosAcreditadora.add(resultadoAcreditadora)
                    i.save()
                elif request.POST[id] == '0' and i in resultadosSelec:
                    i.resultadosAcreditadora.remove(resultadoAcreditadora)
                    i.save()
            flag = 1

        elif request.POST['operacion'] == 'insertar':
            ResultadoAcreditadora.objects.create(codigo=request.POST['codigo'],descripcion=request.POST['descripcion'],
                                                 acreditadora_id=request.POST["acreditadora"])
            resultadoAcreditadora = ResultadoAcreditadora.objects.latest('id')
            pk = resultadoAcreditadora.pk
            for i in resultados:
                id = 'select' + str(i.pk)
                if request.POST[id] == '1':
                    i.resultadosAcreditadora.add(resultadoAcreditadora)
                    i.save()
            flag = 2

    if pk == '0':
        insert = True
    else:
        resultadoAcreditadora = ResultadoAcreditadora.objects.get(pk=pk)
        resultadosSelec = Resultado.objects.filter(resultadosAcreditadora=pk)

    context = {
        'insert': insert,
        'resultadoAcreditadora': resultadoAcreditadora,
        'resultados' : resultados,
        'resultadosSelec': resultadosSelec,
        'flag' : flag,
    }
    return render(request,'gestionarRE/editarRE.html',context)

def eliminarRE(request,pk):

    #Candidate.objects.filter(pk=pk).delete()
    print(request.POST)
    return