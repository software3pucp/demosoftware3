from django.shortcuts import render
import requests
from django.shortcuts import render

# Create your views here.
from aaron.models import Waffles


# Create your views here.


def aaronHome(request):

    wafflesList = Waffles.objects.filter()


    if request.POST:

        if request.POST["tipoform"] == "1":

            Waffles.objects.create(name=request.POST["name"], precio=request.POST["precio"])

        context = {
            'titulo': "Has guardado en BBDD :" + request.POST["name"],
            'listaWaffles': wafflesList,
        }
        return render(request, 'aaron/home.html', context)



    context = {
        'titulo': 'HE ENTRADO POR URL',
        'listaWaffles': wafflesList,
    }


    return render(request, 'aaron/home.html', context)

# Create your views here.
