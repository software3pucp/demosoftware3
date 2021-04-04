from django.shortcuts import render

# Create your views here.

def caliHome(request):
    context = {
        'titulo': 'Hola mundo  cali',
    }
    return render(request, 'cali/home.html', context)



