import requests
from django.shortcuts import render

# Create your views here.
from lozano.models import Language


def lozanoHome(request):

    languages = Language.objects.filter()

    pais = "peru"
    response = requests.get('https://restcountries.eu/rest/v2/name/' + pais)
    capital = response.json()[0]["capital"]

    context = {
        'titulo': 'Modulo Lozano',
        'holaMundo': 'Hola mundo',
        'listaIdiomas': languages,
        'capital': capital
    }
    return render(request, 'lozano/home.html', context)

def lozano404(request):
    return render(request, 'lozano/404.html')