import requests
from django.shortcuts import render

# Create your views here.
#ESTE ES EL BACKEND DEL MÓDULO
from django.views.generic import CreateView


class RenderHome(CreateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        return

def ejemplo(request):
    return render(request, 'ejemplo.html')

