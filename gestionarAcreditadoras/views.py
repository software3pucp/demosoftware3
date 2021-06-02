from django.shortcuts import render

# Create your views here.

def listarAcreditadoras(request):
    context = {

    }
    return render(request,'gestionarAcreditadoras/listarAcreditadoras.html',context)

def editarAcreditadoras(request,pk):
    context = {

    }
    return render(request,'gestionarAcreditadoras/editarAcreditadoras.html',context)