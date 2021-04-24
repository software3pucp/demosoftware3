from django.shortcuts import render
from django.shortcuts import render, redirect
# Create your views here.
from django.shortcuts import render
from ale.models import Personaje
# Create your views here.


def usuario_list(request):
    usuario = Personaje.objects.all()
    return render(request, 'ale/base/lista.html', {'usuario':usuario})

def eliminarPersonajes(request,pk):
    usuario = Personaje.objects.get(pk=pk)
    usuario.delete()
    return redirect(usuario_list)

def editarPersonajes(request,pk):
    usuario = Personaje.objects.get(pk=pk)
    if request.POST:
        print(request.POST)
        newname = request.POST["nombre"]
        newedad = request.POST["edad"]

        usuario.name = newname
        usuario.edad = newedad
        usuario.save()

        return redirect(usuario_list)

    context = {
        'usuario': usuario
    }
    return render(request, 'ale/editar.html', context)

def aleHome(request):
    print(request.POST)

    if request.POST:
        nombre = request.POST["nombre"]
        edad = request.POST["edad"]
        sexo = "M"
        try:
            if request.POST["c2"] == "on":
                sexo = "F"
        except:
            sexo = "M"

        Personaje.objects.create(name=nombre,edad = edad, sexo = sexo)


        return render(request, 'ale/home.html')
    return render(request, 'ale/home.html')
