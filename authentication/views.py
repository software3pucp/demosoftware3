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
        'media_path':media_path
    }
    return render(request, 'authentication/User_list.html', context)


def Register(request):
    if request.POST:
        user = User.objects.create(first_name=request.POST['card-name'],
                            username=request.POST['card-correo'], code=request.POST['card-codigo'],
                            email=request.POST['card-correo'], password=request.POST['card-password'], is_active=True)
        if request.POST['photo']:
            user.photo = request.FILES['photo']
            user.save()
        return redirect(Show)
    return render(request, 'authentication/User_Add.html')

def Edit(request,pk):
    user = User.objects.get(pk=pk)
    if request.POST:
        newname=request.POST['card-name']
        newcode=request.POST['card-codigo']
        newemail=request.POST['card-correo']
        newpassword=password=request.POST['card-password']

        user.first_name=newname
        user.code=newcode
        user.email=newemail
        user.password=newpassword
        user.save()
        
        return redirect(Show)
    
    context = {
        'user':user    
    }
    
    return render(request,'authentication/User_Edit.html',context)