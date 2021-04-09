import requests
from django.shortcuts import render

# Create your views here.
from Jhonatan.models import Language


def usuario_list(request):
    usuario = Language.objects.all()
    return render(request, 'jhonatan/Listado.html', {'usuario':usuario})




def PolarHome(request):
    print("-----------------------------------------------------------------------")
    print(request.POST)
    print("-----------------------------------------------------------------------")
    if request.POST:
        Language.objects.create(name=request.POST["username"], habloElIdioma=False,
                                longitud=len(request.POST["username"]))

        context = {
            'titulo': "Has guardado en BBDD a " + request.POST["username"] + "!!",
            'capital': "POST"
        }
        return render(request, 'jhonatan/home.html', context)

    langList = Language.objects.filter(habloElIdioma=False)
    print("=======================================================================")
    print(langList)
    print("=======================================================================")

    pais = "peru"
    response = requests.get('https://restcountries.eu/rest/v2/name/'+ pais)
    print(response.json())
    print("======================")
    print(response.json()[0]["capital"])
    capital = response.json()[0]["capital"]

    context = {
        'titulo': 'Hola mundo, soy Jhonatan',
        'listaIdiomas': langList,
        'capital' : capital
    }
    return render(request, 'jhonatan/home.html', context)
