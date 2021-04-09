import requests
from django.shortcuts import render, redirect
from candidates2021.models import Candidate

def ListCandidates(request):

    context = {
        'lista': Candidate.objects.all(),
    }
    return render(request,'Candidatos/home.html',context)


def Register(request):
    if request.POST:
        Candidate.objects.create(name=request.POST["name"], partido=request.POST["partido"])
        print(request.POST)
        return redirect(ListCandidates)
    return render(request,'Candidatos/formulario.html')


def Delete(request,pk):

    Candidate.objects.filter(pk=pk).delete()
    print(request.POST)
    return redirect(ListCandidates)

def Edit(request,pk):

    if request.POST:
        candidato = Candidate.objects.get(pk=pk)
        candidato.name = request.POST["name"]
        candidato.partido = request.POST["partido"]
        candidato.save()
        return redirect(ListCandidates)

    context = {
         'candidato':  Candidate.objects.get(pk=pk)
    }
    return render(request, 'Candidatos/formulario.html',context)



