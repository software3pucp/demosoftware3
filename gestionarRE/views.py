from django.shortcuts import render,redirect

from gestionarRE.models import ResultadoAcreditadora, Resultado


# Create your views here.


def listarRE(request):
    resultados = ResultadoAcreditadora.objects.filter(acreditadora=1)
    print(resultados)
    context = {
        'resultados' : resultados,
    }
    return render(request,'gestionarRE/listarRE.html',context)


def editarRE(request,pk):

    if request.POST:
        print(request.POST)

    insert = False
    resultadoAcreditadora = ResultadoAcreditadora()
    resultadoAcreditadora.pk = 0
    resultadosSelec = []

    if pk == '0':
        insert = True
    else:
        resultadoAcreditadora = ResultadoAcreditadora.objects.get(pk=pk)
        resultadosSelec = Resultado.objects.filter(resultadosAcreditadora=pk)

    resultados = Resultado.objects.filter()
    print('*******************************************************************************************************')
    print(resultadosSelec)
    print(resultados)
    print('*******************************************************************************************************')
    context = {
        'insert': insert,
        'resultadoAcreditadora': resultadoAcreditadora,
        'resultados' : resultados,
        'resultadosSelec': resultadosSelec,
    }
    return render(request, 'gestionarRE/editarRE.html', context)

def eliminarRE(request,pk):

    #Candidate.objects.filter(pk=pk).delete()
    print(request.POST)
    return redirect(listarRE)