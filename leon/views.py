import requests
from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.core import serializers

from demosoftware3.settings import MEDIA_URL
from leon.models import Language, LanguageLearned


def leonHome(request):

    langList = Language.objects.filter()
    learnedlist = LanguageLearned.objects.filter(state=0)

    if request.POST:
        selectedLanguage = Language.objects.get(pk=request.POST["seleccion"])
        state = 0
        LanguageLearned.objects.create(language_id=selectedLanguage.pk, state=state)

        ser_instance = serializers.serialize('json', [selectedLanguage, ])
        return JsonResponse({"newLanguage": ser_instance}, status=200)


    context = {
        'listaIdiomas': langList,
        'learnedlist': learnedlist,
    }
    return render(request, 'leon/ajax.html', context)

def leonArchivos(request):

    langList = Language.objects.filter()
    learnedlist = LanguageLearned.objects.filter(state=0)

    if request.POST:
        selectedLanguage = Language.objects.get(pk=request.POST["seleccion"])

        Language.objects.create(name=selectedLanguage.name, foto=request.POST["foto"])
        print(request.POST["foto"])

        context = {
            'listaIdiomas': langList,
            'learnedlist': learnedlist,
            'media_path': MEDIA_URL,
        }
        return render(request, 'leon/archivos.html', context)


    context = {
        'listaIdiomas': langList,
        'learnedlist': learnedlist,
        'media_path': MEDIA_URL,
    }
    return render(request, 'leon/archivos.html', context)


def idiomaDetalle(request, pk):
    idioma = Language.objects.get(pk=pk)

    context = {
        "idiomaDetalle": idioma
    }
    return render(request, 'leon/idiomas/idioma_detalle.html', context)

def ajax(request):
    print(request.POST)
    idioma = Language.objects.get(pk=7)
    ser_instance = serializers.serialize('json', [idioma,])
    return JsonResponse({"respuesta": ser_instance, "datoAdicional": "hola"}, status=200)

