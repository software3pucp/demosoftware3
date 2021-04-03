from django.shortcuts import render

# Create your views here.



def juanHome(request):
    context = {
        'variable': 'Hola mundo Juan',
    }
    return render(request, 'juan/home.html', context)



