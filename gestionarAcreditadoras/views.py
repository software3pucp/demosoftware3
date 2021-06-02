from django.shortcuts import render

# Create your views here.

def listarAcreditadoras(request):
    context = {

    }
    return render(request,'gestionarAcreditadoras/listarAcreditadoras.html',context)

def crearAcreditadoras(request,pk):
    context = {

    }
    return render(request,'gestionarAcreditadoras/crearAcreditadoras.html',context)