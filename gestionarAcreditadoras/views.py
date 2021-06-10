from django.http import JsonResponse
from django.shortcuts import render, redirect
from demosoftware3.settings import MEDIA_URL
import unicodedata

# Create your views here.
from django.core import serializers
from gestionarAcreditadoras.models import Acreditadora


def listarAcreditadoras(request):

    if request.POST:
        if request.POST['operacion'] == 'listAcred':
            acreditadoras = Acreditadora.objects.filter(estado=request.POST['estado'])
            data = serializers.serialize("json", acreditadoras)
            return JsonResponse({"resp": data}, status=200)
        elif request.POST['operacion'] == 'desactivar':
            acreditadora = Acreditadora.objects.get(pk=request.POST['pk'])
            if acreditadora.estado == Acreditadora.ESTADOS[2][0]:
                acreditadora.estado = Acreditadora.ESTADOS[1][0]
            elif acreditadora.estado == Acreditadora.ESTADOS[1][0]:
                acreditadora.estado = Acreditadora.ESTADOS[2][0]
            acreditadora.save()

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
    print('***********************************************************************************************************')
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
            if request.POST['photo_name'] != '':
                acreditadora.foto = request.FILES['photo']
            acreditadora.save()
            return redirect('listarAcreditadoras')

    if pk != '0':
        acreditadora = Acreditadora.objects.get(pk=pk)
    else:
        acreditadora.pk = pk

    context = {
        'acreditadora': acreditadora,
        'media_path': media_path,
    }
    return render(request,'gestionarAcreditadoras/crearAcreditadoras.html',context)

def eliminarAcreditadora(request,pk):
    acreditadora = Acreditadora.objects.get(pk=pk)
    if acreditadora.estado == Acreditadora.ESTADOS[2][0]:
        acreditadora.estado = Acreditadora.ESTADOS[1][0]
    elif acreditadora.estado == Acreditadora.ESTADOS[1][0]:
        acreditadora.estado = Acreditadora.ESTADOS[2][0]
    acreditadora.save()
    print("Correcto desactivar Acreditadora!")
    return redirect('listarAcreditadoras')