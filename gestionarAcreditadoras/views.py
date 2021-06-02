from django.shortcuts import render, redirect
from demosoftware3.settings import MEDIA_URL
import unicodedata

# Create your views here.
from gestionarAcreditadoras.models import Acreditadora


def listarAcreditadoras(request):
    media_path = MEDIA_URL
    context = {
        'ListaAcreditadora': Acreditadora.objects.filter(estado=Acreditadora.ESTADOS[1][0]),
        'ListaAcreditadoraInactivos': Acreditadora.objects.filter(estado=Acreditadora.ESTADOS[2][0]),
        'ListaEstados': Acreditadora.ESTADOS[1:],
        'media_path': media_path
    }
    return render(request,'gestionarAcreditadoras/listarAcreditadoras.html',context)

def crearAcreditadoras(request,pk):
    media_path = MEDIA_URL
    acreditadora = Acreditadora()

    print('***********************************************************************************************************')
    print(request.POST)
    print(request.FILES)
    print('***********************************************************************************************************')

    if request.POST:
        if request.POST['operacion'] == 'insertar':
            nombre = request.POST['nombre']
            foto = request.FILES['photo']
            Acreditadora.objects.create(nombre=nombre,foto=foto)
            return redirect('listarAcreditadoras')
        elif request.POST['operacion'] == 'editar':
            acreditadora = Acreditadora.objects.get(pk=pk)
            acreditadora.nombre = request.POST['nombre']
            acreditadora.foto = request.FILES['photo']
            acreditadora.save()

    if ( int(pk) > 0):
        acreditadora = Acreditadora.objects.get(pk=pk)
    else:
        acreditadora.pk = pk

    context = {
        'acreditadora': acreditadora,
        'media_path': media_path,
    }
    return render(request,'gestionarAcreditadoras/crearAcreditadoras.html',context)

def eliminarAcreditadora(request, id_acreditadora):
    acreditadora = Acreditadora.objects.get(pk=id_acreditadora)
    acreditadora.estado = Acreditadora.ESTADOS[2][0]
    acreditadora.save()
    print("Correcto desactivar Acreditadora!")
    return redirect('listarAcreditadoras')