import requests
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.core import serializers

from leon.models import Language, LanguageLearned


def leonHome(request):

    langList = Language.objects.filter()
    learnedlist = LanguageLearned.objects.filter(state=0)

    if request.POST:
        selectedLanguage = Language.objects.get(pk=request.POST["seleccion"])
        state = 0
        LanguageLearned.objects.create(language_id=selectedLanguage.pk, state=state)
        ser_instance = serializers.serialize('json', [selectedLanguage, ])
        print(ser_instance)
        return JsonResponse({"newLanguage": ser_instance}, status=200)


    context = {
        'listaIdiomas': langList,
        'learnedlist': learnedlist
    }
    return render(request, 'leon/home.html', context)


def idiomaDetalle(request, pk):
    idioma = Language.objects.get(pk=pk)

    context = {
        "idiomaDetalle": idioma
    }
    return render(request, 'leon/idiomas/idioma_detalle.html', context)