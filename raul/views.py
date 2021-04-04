from django.shortcuts import render

# Create your views here.



def raulHome(request):
    context = {
        'titulo': 'Raul',
    }
    return render(request, 'raul/home.html', context)


