from django.shortcuts import render, redirect

# Create your views here.

import requests
from django.views.generic import CreateView
from authentication.models import User


def Show(request):
    context = {
        'users': User.objects.all(),
    }
    return render(request, 'authentication/User_list.html', context)


def Register(request):
    if request.POST:
        User.objects.create(photo=request.FILES['photo'], first_name=request.POST['card-name'],
                            username=request.POST['card-correo'], code=request.POST['card-codigo'],
                            email=request.POST['card-correo'], password=request.POST['card-password'], is_active=True)
        return redirect(Show)
    return render(request, 'authentication/User_Add.html')
