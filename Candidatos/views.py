import requests
from django.shortcuts import render
from Candidatos.models import Candidate

def ListCandidates(request):

    # if request.POST:
    #     Champion.objects.create(name=request.POST["name"], price=request.POST["price"],
    #                             tipo=request.POST["tipo"],foto=request.POST["foto"])
    #
    #     context = {
    #         'titulo': "Has guardado en BBDD :" + request.POST["name"],
    #     }
    #     return render(request, 'raul/home.html', context)

    context = {
        'listaCandidatos': Candidate.objects.all(),
    }
    return render(request,'home.html',context)


def championDetalle(request, pk):
    champion = Champion.objects.get(pk=pk)

    context = {
        "champion": champion
    }
    return render(request, 'raul/champion.html', context)


