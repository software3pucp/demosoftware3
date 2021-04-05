import requests
from django.shortcuts import render

# Create your views here.
from lozano.models import Language, Pais, PaisIdioma


def lozanoHome(request):
    pais = ""
    capital = ""
    key = ""
    found = False
    if request.POST:
        print(request.POST["nombrePais"])
        response = requests.get('https://restcountries.eu/rest/v2/name/' + request.POST["nombrePais"])
        if response.status_code != 404:
            pais = response.json()[0]["name"]
            capital = response.json()[0]["capital"]
            paises = Pais.objects.filter(name=pais)
            if len(paises) == 0:
                Pais.objects.create(name=pais,capital=capital)
                key = Pais.objects.filter(name=pais)[0].pk
            else:
                key = Pais.objects.filter(name=pais)[0].pk
            found = True

    context = {
        'titulo': 'Modulo Lozano',
        'holaMundo': 'Hola mundo',
        'key': key,
        'pais': pais,
        'capital': capital,
        'found': found
    }
    return render(request, 'lozano/home.html', context)

def lozanoIdiomas(request):
    idioma = ""
    insert = False
    found = False
    if request.POST:
        print(request.POST["nombreIdioma"])
        idiomas = Language.objects.filter(name=request.POST["nombreIdioma"])
        if len(idiomas) != 0:
            idioma = Language.objects.filter(name=request.POST["nombreIdioma"])[0]
            found = True

    context = {
        'titulo': 'Modulo Lozano',
        'idioma': idioma,
        'found': found,
        'inser': insert
    }
    return render(request, 'lozano/idiomas/idiomas.html', context)

def lozano404(request):
    return render(request, 'lozano/404.html')

def lozanoIdioma(request,pk):

    idioma = Language.objects.get(pk=pk)

    context = {
        "idiomaDetalle": idioma
    }
    return render(request, 'lozano/idiomas/idioma.html',context)

def lozanoPais(request, pk):
    if request.POST:
        idiomas = Language.objects.filter(name=request.POST["idioma"])
        if len(idiomas) == 0:
            Language.objects.create(name=request.POST["idioma"], habloElIdioma=False,longitud=len(request.POST["idioma"]))
            lenguaje = Language.objects.get(name=request.POST["idioma"])
            PaisIdioma.objects.create(idLanguage=lenguaje.pk, idPais=pk)
        else:
            lenguaje = Language.objects.filter(name=request.POST["idioma"])[0]
            PaisIdioma.objects.create(idLanguage=lenguaje.pk, idPais=pk)
    pais = Pais.objects.get(pk=pk)
    langList = PaisIdioma.objects.filter(idPais=pk)
    print(langList)
    lista = []
    for idioma in langList:
        lista.append(Language.objects.get(pk=idioma.idLanguage))
    context = {
        "pais": pais,
        'listaIdiomas': lista
    }
    return render(request, 'lozano/paises/pais.html', context)