from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.



def aleHome(request):
    context = {
        'titulo': 'Hola mundo',
    }
    return render(request, 'ale/home.html', context)
