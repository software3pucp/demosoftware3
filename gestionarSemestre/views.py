from django.shortcuts import render

# Create your views here.
from datetime import datetime
from gestionarSemestre.models import Semestre

def listarSemestre(request):
    semestreLista = Semestre.objects.filter()

    context = {
        'ListaSemestre':semestreLista

    }
    return render(request,'gestionarSemestre/listarSemestre.html',context)
