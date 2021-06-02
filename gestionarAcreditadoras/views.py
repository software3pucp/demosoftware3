from django.shortcuts import render
import unicodedata

# Create your views here.
from gestionarAcreditadoras.models import Acreditadora


def listarAcreditadoras(request):
    context = {

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