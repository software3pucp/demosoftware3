import requests
from django.shortcuts import render
from gestionarREAcreditadoras.models import Acreditadora,ResultadoAcreditadora
from gestionarIndicadores.models import Indicador

# Create your views here.


def listarRE(request):
    resultados = ResultadoAcreditadora.objects.filter(acreditadora=1)
    context = {
        'resultados' : resultados,
    }
    return render(request,'gestionarREAcreditadoras/listarRE.html',context)


def editarRE(request,pk):
    insert = False
    flag = 0
    resultadoAcreditadora = ResultadoAcreditadora()
    resultadoAcreditadora.pk = pk


    indicadores=Indicador.objects.filter()
    print(indicadores)

    if request.POST:
        print(request.POST)
        if request.POST['operacion'] == 'entrada':
            resultadoAcreditadora.acreditadora_id = request.POST["acreditadora"]

        elif request.POST['operacion'] == 'editar':

            resultadoAcreditadora = ResultadoAcreditadora.objects.get(pk=pk)
            resultadoAcreditadora.codigo = request.POST['codigo']
            resultadoAcreditadora.descripcion = request.POST['descripcion']
            resultadoAcreditadora.save()
            flag = 1

        elif request.POST['operacion'] == 'insertar':
            codigo = request.POST['codigo']
            descripcion = request.POST['descripcion']
            # acreditadora_id = request.POST["acreditadora"]
            # acreditadora_id = 1
            print("AYUDAAAAAAAAAAAA")
            ResultadoAcreditadora.objects.create(codigo=codigo,descripcion=descripcion)
            print("AYUDA")
            # resultadoAcreditadora = ResultadoAcreditadora.objects.latest('id')
            # pk = resultadoAcreditadora.pk
            flag = 2

    if pk == '0':
        insert = True
    else:
        resultadoAcreditadora = ResultadoAcreditadora.objects.get(pk=pk)

    context = {
        'insert': insert,
        'resultadoAcreditadora': resultadoAcreditadora,
        'indicadores': indicadores,
        'flag' : flag,
    }
    return render(request,'gestionarREAcreditadoras/editarRE.html',context)

def eliminarRE(request,pk):

    #Candidate.objects.filter(pk=pk).delete()
    print(request.POST)
    return