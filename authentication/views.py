from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse

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
        roles = request.POST.getlist('choices-multiple-remove-button')
        for val in roles:
            group = Group.objects.get(id=val)
            group.user_set.add(user)
        return redirect(Show)
    return render(request, 'authentication/User_Add.html', context)


def Edit(request, pk):
    media_path = MEDIA_URL
    user = User.objects.get(pk=pk)
    print(request.POST)
    if request.POST:
        newname = request.POST['card-name']
        newcode = request.POST['card-codigo']
        newemail = request.POST['card-correo']
        newpassword = request.POST['card-password']
        if request.FILES.get('photo'):
            newphoto = request.FILES.get('photo')
            user.photo = newphoto

        user.first_name = newname
        user.code = newcode
        user.email = newemail
        user.password = newpassword
        user.save()
        if request.POST.getlist('choices-multiple-remove-button'):
            user.groups.clear()
            roles = request.POST.getlist('choices-multiple-remove-button')
            for val in roles:
                group = Group.objects.get(id=val)
                group.user_set.add(user)

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
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(select_rol)
        else:
            print('Dentro de usuario no registrado')
            error_message = "Ha surgido un error en el inicio de sesión en usuario y/o contraseña. "+ \
                            "Si no cuenta con un usuario, comuníquese con el administrador"
            context = {
                'error_message': error_message,
            }
            return render(request, 'authentication/login.html', context)

    return render(request, 'authentication/login.html')


def sing_out(request):
    user = User.objects.get(pk=request.user.pk)
    user.rol_actual = None
    user.save()
    logout(request)
    return redirect(sing_in)


def select_rol(request):
    user = User.objects.get(pk=request.user.pk)
    context = {
        'roles': list(user.groups.values_list())
    }
    if request.POST:
        # -- elegir roles
        pk = request.POST['rol_actual']
        print("======================================")
        print(pk)
        aux = Group.objects.filter(pk=pk)
        user.rol_actual = aux[0].name
        user.save()
        return JsonResponse({}, status=200)
    return render(request, 'authentication/Select_Rol.html', context)


def validation(request):
    return redirect(listarFacultad)


def social_sign_in(request):
    print("Entra a social_sign_in:")
    print(request.POST)
    email = request.POST['email']

    try:
        user = User.objects.get(username=email)

    except User.DoesNotExist:
        print("Usuario no existe")
        noRegistrado =True
        error_message = "Ha surgido un error en el inicio de sesión en usuario y/o contraseña. " + \
                        "Si no cuenta con un usuario, comuníquese con el administrador"
        url = reverse('login')
        return JsonResponse({"url": url, "noRegistrado":noRegistrado, "error_message":error_message}, safe=False)
    else:
        print(user.password)
        login(request, user)
        noRegistrado = False
        url = reverse('listarFacultad')
        return JsonResponse({"url": url, "noRegistrado":noRegistrado}, safe=False)
