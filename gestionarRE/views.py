from django.shortcuts import render

# Create your views here.

def listarRE(request):
    context = {

    }
    return render(request,'gestionarRE/listarRE.html',context)