from django.shortcuts import render

# Create your views here.



def gilmerHome(request):
    context = {
        'titulo': 'Hola mundo, software grupo 3',
    }
    return render(request, 'gilmer/home.html', context)

