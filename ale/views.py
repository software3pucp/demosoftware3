from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from ale.models import Personaje
# Create your views here.


def usuario_list(request):
    usuario = Personaje.objects.all()
    return render(request, 'ale/base/lista.html', {'usuario':usuario})

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
