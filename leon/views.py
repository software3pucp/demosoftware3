import requests
from django.shortcuts import render

# Create your views here.
from leon.models import Language


def leonHome(request):

    print("-----------------------------------------------------------------------")
    print(request.POST)
    print("-----------------------------------------------------------------------")
    if request.POST:
        Language.objects.create(name=request.POST["username"], habloElIdioma=False,
                                longitud=len(request.POST["username"]))

        context = {
            'titulo': "Has guardado en BBDD :" + request.POST["username"],
            'capital': "POST"
        }
        return render(request, 'leon/home.html', context)

    langList = Language.objects.filter()
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
        'capital' : capital
    }
    return render(request, 'leon/home.html', context)


def idiomaDetalle(request, pk):
    idioma = Language.objects.get(pk=pk)

    context = {
        "idiomaDetalle": idioma
    }
    return render(request, 'leon/idiomas/idioma_detalle.html', context)