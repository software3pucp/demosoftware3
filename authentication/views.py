from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse
from django.views.generic import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

import requests
from django.views.generic import CreateView
from authentication.models import User
from demosoftware3.settings import MEDIA_URL
from gestionarFacultad.views import listarFacultad
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.models import Group
from authentication.forms import  ResetPasswordForm
from demosoftware3 import settings
import  uuid
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.template.loader import render_to_string


def Show(request):
    media_path = MEDIA_URL
    context = {
        'users': User.objects.all(),
        'media_path': media_path
    }
    return render(request, 'authentication/User_List.html', context)

def EnviarCorreoBienvenida(request, user,p):
    try:
        URL = settings.DOMAIN if not settings.DEBUG else request.META['HTTP_HOST']
        print(type(p))
        print("==========================================")
        mailServer = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        mailServer.starttls()
        mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)

        email_to = user.email
        mensaje = MIMEMultipart()
        mensaje['From'] = settings.EMAIL_HOST_USER
        mensaje['To'] = email_to
        mensaje['Subject'] = 'Bienvenido a Apolo PUCP'

        content = render_to_string('authentication/welcome_email.html', {
            'user': user,
            'password': p,
            'link_home': 'http://{}'.format(URL)
        })
        mensaje.attach(MIMEText(content, 'html'))

        mailServer.sendmail(settings.EMAIL_HOST_USER,
                            email_to,
                            mensaje.as_string())
    except:
        print("error al enviar correo")

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
        p=request.POST['card-password']
        roles = request.POST.getlist('choices-multiple-remove-button')
        i = 0
        for val in roles:
            i += 1
            group = Group.objects.get(id=val)
            group.user_set.add(user)
        if (i==1):
            user.n_Roles = '1'
            user.save()
        EnviarCorreoBienvenida(request, user, p)
        return redirect(Show)
    return render(request, 'authentication/User_Add.html', context)


def Edit(request, pk):
    flag1= False
    flag2= False
    media_path = MEDIA_URL
    i=0
    user = User.objects.get(pk=pk)
    current_user = user.username
    current_contra = user.password
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
        if user.email != newemail:
            flag1 = True
            user.email = newemail
            user.username = newemail

        if newpassword != '':
            flag2 = True
            user.set_password(newpassword)

        if user.pk == request.user.pk and flag1:
            current_user = user.username

        if user.pk == request.user.pk and flag2:
            current_contra = newpassword

        user.save()
        if user.pk == request.user.pk and (flag1 or flag2):
            user = authenticate(request, username=current_user, password=current_contra)
            login(request, user)

        if request.POST.getlist('choices-multiple-remove-button'):
            if (not user.groups is None):
                user.groups.clear()
            roles = request.POST.getlist('choices-multiple-remove-button')
            for val in roles:
                i += 1
                group = Group.objects.get(id=val)
                group.user_set.add(user)
            if (i==1):
                user.n_Roles = '1'
                user.save()
            else:
                user.n_Roles = None
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
    lista = list(user.groups.values_list())
    context = {
        'roles': list(user.groups.values_list())
    }

    if (len(lista)==1):
        pk = lista[0][0]
        name = lista[0][1]
        user.rol_actual = name
        user.save()
        if(pk==1):
            return redirect('showUsers')
        elif (pk==2):
            return redirect('listarFacultad')
        elif (pk==3):
            return redirect('showUsers')
        elif (pk==4):
            return redirect('listarSemestre')
        elif (pk==5):
            return redirect('listarFacultad')
        elif (pk==6):
            return redirect('listarSemestreDocente')
        else:
            return redirect('listarFacultad')

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

class ResetPasswordView(FormView):

    form_class = ResetPasswordForm
    template_name = 'authentication/resetPassword.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def send_email_reset_pwd(self, user):
        data = {}
        try:
            URL = settings.DOMAIN if not settings.DEBUG else self.request.META['HTTP_HOST']
            user.token = uuid.uuid4()
            user.save()

            mailServer = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
            mailServer.starttls()
            mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)

            email_to = user.email
            mensaje = MIMEMultipart()
            mensaje['From'] = settings.EMAIL_HOST_USER
            mensaje['To'] = email_to
            mensaje['Subject'] = 'Reseteo de contraseña'

            content = render_to_string('authentication/send_email.html', {
                'user': user,
                'link_resetpwd': 'http://{}/login/change/password/{}/'.format(URL, str(user.token)),
                'link_home': 'http://{}'.format(URL)
            })
            mensaje.attach(MIMEText(content, 'html'))

            mailServer.sendmail(settings.EMAIL_HOST_USER,
                                email_to,
                                mensaje.as_string())
        except Exception as e:
            data['error'] = str(e)
        return data

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            form = ResetPasswordForm(request.POST)
            if form.is_valid():
                user = form.get_user()
                data = self.send_email_reset_pwd(user)
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data,safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reseteo de Contraseña'
        return context