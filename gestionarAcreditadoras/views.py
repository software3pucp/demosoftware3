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
    acreditadora = Acreditadora()
    acreditadora.pk = pk

    if request.POST:
        if request.POST['operacion'] == 'entrada':
            print('Insertar')

    context = {
        'acreditadora': acreditadora,
    }
    return render(request,'gestionarAcreditadoras/crearAcreditadoras.html',context)

def eliminarAcreditadora(request, id_acreditadora):
    acreditadora = Acreditadora.objects.get(pk=id_acreditadora)
    acreditadora.estado = Acreditadora.ESTADOS[2][0]
    acreditadora.save()
    print("Correcto desactivar Acreditadora!")
    return redirect('listarAcreditadoras')