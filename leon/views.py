import requests
from django.shortcuts import render

# Create your views here.
from leon.models import Language


def leonHome(request):

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
        'titulo': 'Hola mundo',
        'listaIdiomas': langList,
        'capital' : capital
    }
    return render(request, 'leon/home.html', context)




