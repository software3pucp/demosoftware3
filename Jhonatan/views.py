from django.shortcuts import render

# Create your views here.



def PolarHome(request):
    context = {
        'titulo': 'Hola mundo, Soy Jhonatan',
    }
    return render(request, 'jhonatan/home.html', context)



