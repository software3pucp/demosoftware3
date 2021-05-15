from django.shortcuts import render

# Create your views here.

def listarCursos(request):
    facultad = "Ingenieria Informática"
    estados = ["Activo","Inactivo"]
    context = {
        'facultad' : facultad,
        'estados' : estados
    }
    return render(request,'gestionarPlanMedicion/listarCursos.html',context)

def editarCursos(request):
    context = {

    }
    return render(request,'gestionarPlanMedicion/editarCursos.html',context)

