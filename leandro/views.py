import requests
from django.shortcuts import render

# Create your views here.
from leandro.models import Prueba


def leandroHome(request):

    print("-----------------------------------------------------------------------")
    print(request.POST)
    print("-----------------------------------------------------------------------")
    if request.POST:

        Prueba.objects.create(name=request.POST["username"], habloElIdioma=False, longitud= len(request.POST["username"]))

        context = {
            'titulo': "Has guardado en BBDD :" + request.POST["username"],
            'capital': "POST"
        }
        return render(request, 'leandro/home.html', context)

    langList = Prueba.objects.filter()
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
        'titulo': 'HE ENTADO POR URL',
        'listaIdiomas': langList,
        'capital' : capital,
        'body':'soy un string',
    }
    return render(request, 'leandro/home.html', context)


def idiomaDetalle(request, pk):
    idioma = Prueba.objects.get(pk=pk)

    context = {
        "idiomaDetalle": idioma
    }
    return render(request, 'leandro/idiomas/idioma_detalle.html', context)