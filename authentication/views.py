from django.shortcuts import render, redirect

# Create your views here.

import requests
from django.views.generic import CreateView
from authentication.models import User
from demosoftware3.settings import MEDIA_URL


def Show(request):
    media_path = MEDIA_URL
    context = {
        'users': User.objects.all(),
        'media_path': media_path
    }
    return render(request, 'authentication/User_list.html', context)


def Register(request):
    if request.POST:
        photo = request.FILES['photo']
        user = User.objects.create_user(first_name=request.POST['card-name'],
                                        username=request.POST['card-correo'], code=request.POST['card-codigo'],
                                        email=request.POST['card-correo'], password=request.POST['card-password'],
                                        photo=photo, is_active=True)
        return redirect(Show)
    return render(request, 'authentication/User_Add.html')


def Edit(request, pk):
    user = User.objects.get(pk=pk)
    if request.POST:
        newname = request.POST['card-name']
        newcode = request.POST['card-codigo']
        newemail = request.POST['card-correo']
        newpassword = request.POST['card-password']

        user.first_name = newname
        user.code = newcode
        user.email = newemail
        user.password = newpassword
        user.save()

        return redirect(Show)

    context = {
        'user': user
    }

    return render(request, 'authentication/User_Edit.html', context)


def Delete(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return redirect(Show)
