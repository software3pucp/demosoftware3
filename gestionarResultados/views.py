import requests
from django.shortcuts import render

# Create your views here.
from gestionarIndicadores.models import Indicador
from gestionarResultados.models import ResultadoPUCP


def crearResultado(request):
     registrado=False
     if request.POST:
         newResultado =ResultadoPUCP.objects.create(codigo=request.POST['codigo'], descripcion=request.POST['descripcion'])
         registrado = True
         context = {
             'registrado': registrado,
             'newResultado':newResultado,
         }
         return listarIndicadoresxResultado(request,id_Resultado=newResultado.pk)

     context = {
         'registrado': registrado,
     }
     return render(request, 'gestionarResultados/crearResultado.html', context)

def listarResultado(request):
    resultados = ResultadoPUCP.objects.filter()
    context = {
        'resultados' : resultados,
    }
    return render(request,'gestionarResultados/listarResultados.html',context)

def editarResultado(request, pk):
    flag = False
    if request.POST:
        resultado = ResultadoPUCP.objects.get(pk=pk)
        resultado.codigo = request.POST['codigo']
        resultado.descripcion = request.POST['descripcion']
        resultado.save()
        flag = True

    resultado= ResultadoPUCP.objects.get(pk=pk)
    context = {
        'resultado': resultado,
        'flag': flag,
    }
    return listarIndicadoresxResultado(request, id_Resultado=resultado.pk)

def listarIndicadoresxResultado(request, id_Resultado):
    context = {
        'listaIndicadores': Indicador.objects.filter(resultado_id=id_Resultado),
        'listaResultado': ResultadoPUCP.objects.all(),
        'resultado' : ResultadoPUCP.objects.get(pk=id_Resultado)
    }
    return render(request, 'gestionarIndicadores/listarIndicadorxResultado.html', context)
