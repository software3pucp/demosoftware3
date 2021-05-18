import requests
from django.shortcuts import render, redirect
from django.db.models import Q
# Create your views here.
from gestionarIndicadores.models import Indicador
from gestionarResultados.models import ResultadoPUCP

def crearResultado(request):
     registrado=False
     if request.POST:
         newResultado =ResultadoPUCP.objects.create(codigo=request.POST['codigo'], descripcion=request.POST['descripcion'])
         return redirect('editarResultado', pk=newResultado.pk)

     context = {
         'registrado': registrado,
     }
     return render(request, 'gestionarResultados/crearResultado.html', context)

def listarResultado(request):
    eliminado = False
    if request.POST:
        resultadoPk = request.POST['resultadoPk']
        resultado = ResultadoPUCP.objects.get(pk=resultadoPk)
        resultado.estado ='0' #eliminación lógica
        resultado.save()
        eliminado =True

    resultados = ResultadoPUCP.objects.filter(Q(estado='1') | Q(estado='2'))
    context = {
        'resultados' : resultados,
    }
    return render(request,'gestionarResultados/listarResultados.html',context)

def editarResultado(request, pk):
    flag = 0
    if request.POST:
        print('------------------------------------------------')
        print(request.POST)
        print('------------------------------------------------')
        resultado = ResultadoPUCP.objects.get(pk=pk)
        resultado.codigo = request.POST['codigo']
        resultado.descripcion = request.POST['descripcion']
        resultado.save()
        flag = True

    context = {
        'listaIndicadores': Indicador.objects.filter(resultado_id=pk,estado=1),
        'listaResultado': ResultadoPUCP.objects.all(),
        'resultado' : ResultadoPUCP.objects.get(pk=pk),
        'flag': flag
    }
    return render(request, 'gestionarIndicadores/listarIndicadorxResultado.html', context)
