from django.shortcuts import render, redirect

# Create your views here.

import requests
from django.views.generic import CreateView
from authentication.models import User
from authentication.forms import UserForm

class RenderLogin(CreateView):
    template_name = 'authentication/login.html'

    def get_context_data(self, **kwargs):
        context = {

        }
        return context

#Codigo: 09/05/2021 JACM

class RegisterUser(CreateView):
    model = User
    template = 'authentication/User_Add.html'

    def get(self, request, *args, **kwargs):
        user_form = UserForm()
        context = {
            'user_form': user_form
        }
        return render(request, self.template, context)

    def post(self, request, *args, **kwargs):
        data = self.request.POST
        user_form = UserForm(data=data)
        if user_form.is_valid():
            return redirect('sign_in')
        else:
            errors = user_form.errors
            context = {
                'user_form': user_form,
                'errors': errors
            }
            return render(request, self.template, context)