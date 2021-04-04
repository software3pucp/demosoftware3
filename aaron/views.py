from django.shortcuts import render

# Create your views here.



def aaronHome(request):
    context = {
        'titulo': 'Hola mundo',
    }
    return render(request, 'aaron/home.html', context)
from django.shortcuts import render

# Create your views here.
