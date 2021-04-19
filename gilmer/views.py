from django.shortcuts import render

# Create your views here.
from gilmer.models import Pubgmteams


def gilmerHome(request):
    flag = False
    if request.POST:
        pubgmteam = Pubgmteams.objects.get(pk=request.POST['pubgmTeampk'])
        pubgmteam.estado = 0
        pubgmteam.save()
        flag = True
    teams = Pubgmteams.objects.filter(estado=1)
    context = {
        'teamsList': teams,
        'flag': flag,
    }
    return render(request, 'gilmer/home.html', context)

def insertarPubgmTeam(request):

    registrado = False
    if request.POST:
        Pubgmteams.objects.create(name=request.POST['name'], numPlayers=request.POST['numPlayers'],
                                   region=request.POST['region'], igl=request.POST['igl'],
                                   scout=request.POST['scout'], carry=request.POST['carry'],
                                   support=request.POST['support'],sniper=request.POST['sniper'])
        registrado = True
    context = {
        'registrado' : registrado,
    }
    return render(request, 'gilmer/insertar_pubgmTeam.html', context)

def detallePubgmTeam(request,pk):
    pubgmTeam = Pubgmteams.objects.get(pk=pk)
    context = {
        'pubgmTeam' : pubgmTeam,
    }
    return render(request, 'gilmer/detalle_pubgmTeam.html', context)



def editarPubgmTeam(request,pk):
    flag = False
    if request.POST:
        pubgmTeam = Pubgmteams.objects.get(pk=pk)
        pubgmTeam.name = request.POST['name']
        pubgmTeam.numPlayers = request.POST['numPlayers']
        pubgmTeam.region = request.POST['region']
        pubgmTeam.igl = request.POST['igl']
        pubgmTeam.carry = request.POST['carry']
        pubgmTeam.scout = request.POST['scout']
        pubgmTeam.sniper = request.POST['sniper']
        pubgmTeam.support = request.POST['support']
        pubgmTeam.save()
        flag = True
    pubgmTeam = Pubgmteams.objects.get(pk=pk)
    context = {
        'pubgmTeam': pubgmTeam,
        'flag': flag,
    }
    return render(request, 'gilmer/editar_pubgmTeam.html', context)


