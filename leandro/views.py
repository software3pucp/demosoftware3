
from django.shortcuts import render

# Create your views here.

def leandroHome(request):
    context = {
        'body': 'Hola mundo  zzzz',
    }
    return render(request, 'leandro/home.html', context)

