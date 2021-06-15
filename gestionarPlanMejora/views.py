from django.shortcuts import render

# Create your views here.
from gestionarPlanMejora.models import EstadoActividad


def crearActividad(request):

    estados = EstadoActividad.objects.filter()

    context = {

    }
    return render(request, 'gestionarPlanMejora/crearActividad.html', context)

def editarActividad(request):

    context = {

    }
    return render(request, 'gestionarPlanMejora/editarActividad.html', context)
def subirEvidencia(request):

    context = {

    }
    return render(request, 'gestionarPlanMejora/subirEvidencia.html', context)

def editarEvidencia(request):

    context = {

    }
    return render(request, 'gestionarPlanMejora/editarEvidencia.html', context)