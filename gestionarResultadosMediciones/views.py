from django.shortcuts import render

# Create your views here.

def resultadosMediciones(request):

    context = {

    }
    return render(request,'gestionarResultadosMediciones/resultadosMediciones.html',context)