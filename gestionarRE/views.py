import requests
from django.shortcuts import render
from gestionarRE.models import Acreditadora,ResultadoAcreditadora

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

    if request.POST:
        if request.POST['operacion'] == 'entrada':
            resultadoAcreditadora.acreditadora_id = request.POST["acreditadora"]

        elif request.POST['operacion'] == 'editar':
            resultadoAcreditadora = ResultadoAcreditadora.objects.get(pk=pk)
            resultadoAcreditadora.codigo = request.POST['codigo']
            resultadoAcreditadora.descripcion = request.POST['descripcion']
            resultadoAcreditadora.save()
            flag = 1

        elif request.POST['operacion'] == 'insertar':
            ResultadoAcreditadora.objects.create(codigo=request.POST['codigo'],descripcion=request.POST['descripcion'],
                                                 acreditadora_id=request.POST["acreditadora"])
            resultadoAcreditadora = ResultadoAcreditadora.objects.latest('id')
            pk = resultadoAcreditadora.pk
            flag = 2

    if pk == '0':
        insert = True
    else:
        resultadoAcreditadora = ResultadoAcreditadora.objects.get(pk=pk)

    context = {
        'insert': insert,
        'resultadoAcreditadora': resultadoAcreditadora,
        'flag' : flag,
    }
    return render(request,'gestionarRE/editarRE.html',context)

def eliminarRE(request,pk):

    #Candidate.objects.filter(pk=pk).delete()
    print(request.POST)
    return