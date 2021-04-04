from django.shortcuts import render

# Create your views here.



def lozanoHome(request):
    context = {
        'titulo': 'Modulo Lozano',
        'holaMundo': 'Hola mundo',
    }
    return render(request, 'lozano/home.html', context)