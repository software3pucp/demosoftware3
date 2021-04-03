from django.shortcuts import render

# Create your views here.

def murilloHome(request):
    context = {
        'titulo': 'Hola murillo',
    }
    return render(request, 'murillo/home.html', context)