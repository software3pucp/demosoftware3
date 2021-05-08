import requests
from home.models import Language
from django.shortcuts import render

# Create your views here.
#ESTE ES EL BACKEND DEL MÓDULO
from django.views.generic import CreateView


class RenderHome(CreateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        url = "https://restcountries.eu/rest/v2/name/per"
        response = requests.get(url)
        print("Respuesta del API")

        lang = []
        for i in range(len(response.json())):
            lang.append(response.json()[i]['languages'][0]['name'])


        #Importación de datos de BBDD
        languagesList = Language.objects.filter()
        print("LENGUAGES! ----------")
        for item in languagesList:
            print(item.name)

        context = {
            "languagesList": languagesList,
        }
        return context

def base(request):
    return render(request, 'home/base/home_base.html')

