from django.shortcuts import render

# Create your views here.

import requests
from django.shortcuts import render

# Create your views here.
from cali.models import Candidato

def caliHome(request):

    if request.POST:
        Candidato.objects.create(nombre=request.POST["nombre"],
                                 nombCandidato=request.POST["nombreCandidato"],
                                 postura=request.POST["postura"],
                                 fecha=request.POST["fecha"])


        context = {
            'titulo': "Has guardado en BBDD :" + request.POST["nombre"],
            'capital': "POST"
        }
        return render(request, 'cali/home.html', context)

    langList = Candidato.objects.filter()
    context = {
        'titulo': 'HE ENTADO POR URL',
        'listaCandidatos': langList
    }
    return render(request, 'cali/home.html', context)

def candidatoDetalle(request,pk):
    candidato = Candidato.objects.get(pk=pk)
    context = {
        "candidatoDetalle": candidato
    }
    return render(request , 'cali/candidatos/candidatoDetalle.html',context)

def eliminarCandidato(request, pk):
    Candidato.objects.filter(pk=pk).delete()
    context={
        "eliminarCandidato": Candidato.objects.filter()
    }
    return render(request,'cali/home.html',context)

