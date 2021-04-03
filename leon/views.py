from django.shortcuts import render

# Create your views here.



def leonHome(request):
    context = {
        'titulo': 'Hola mundo',
    }
    return render(request, 'leon/home.html', context)




