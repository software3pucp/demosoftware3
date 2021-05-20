from django.shortcuts import render, redirect

# Create your views here.

import requests
from django.views.generic import CreateView
from authentication.models import User
from demosoftware3.settings import MEDIA_URL
from gestionarFacultad.views import listarFacultad
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.models import Group

def Show(request):
    media_path = MEDIA_URL
    context = {
        'users': User.objects.all(),
        'media_path': media_path
    }
    return render(request, 'authentication/User_list.html', context)


def Register(request):
    context = {
        'grupos': Group.objects.all()
    }
    if request.POST:
        print(request.POST)
        photo = request.FILES.get('photo')
        user = User.objects.create_user(first_name=request.POST['card-name'],
                                        username=request.POST['card-correo'], code=request.POST['card-codigo'],
                                        email=request.POST['card-correo'], password=request.POST['card-password'],
                                        photo=photo, is_active=True)
        roles=request.POST.getlist('choices-multiple-remove-button')
        for val in roles:
            group = Group.objects.get(id=val)
            group.user_set.add(user)
        return redirect(Show)
    return render(request, 'authentication/User_Add.html',context)


def Edit(request, pk):
    media_path = MEDIA_URL
    user = User.objects.get(pk=pk)

    if request.POST:
        newname = request.POST['card-name']
        newcode = request.POST['card-codigo']
        newemail = request.POST['card-correo']
        newpassword = request.POST['card-password']
        newphoto = request.FILES.get('photo')
        user.groups.clear()
        roles = request.POST.getlist('choices-multiple-remove-button')
        for val in roles:
            group = Group.objects.get(id=val)
            group.user_set.add(user)

        user.first_name = newname
        user.code = newcode
        user.email = newemail
        user.password = newpassword
        user.photo = newphoto
        user.save()

        return redirect(Show)

    context = {
        'user': user,
        'media_path': media_path,
        'roles': list(user.groups.values_list()),
        'grupos': Group.objects.all()
    }

    return render(request, 'authentication/User_Edit.html', context)


def Delete(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return redirect(Show)


def sing_in(request):

    if request.POST:
        username = request.POST['card-email']
        password = request.POST['card-password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(listarFacultad)
        else:
            return render(request,'authentication/login.html')

    return render(request,'authentication/login.html')

def sing_out(request):
    logout(request)
    return redirect(sing_in)

def select_rol(request):
    return render(request, 'authentication/Select_rol.html')