from django.shortcuts import render

# Create your views here.


def listarAlumno(request):
    return render(request, 'gestionarEvaluacion/baseEvaluacion/base.html')
