#ESTOS SON LOS URLS DEL MÓDULO
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import  LoginView,LogoutView
from authentication import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)
    path('login/',views.sing_in, name="login"),
    path('logout/', views.sing_out, name="logout"),
    path('add/', views.Register, name='user'),
    path('',views.Show, name='showUsers'),
    path('edit/<pk>', views.Edit, name='editUsers'),
    path('del/<pk>', views.Delete, name='deleteUser'),
    path('select_rol/',views.select_rol, name="selectrol"),
    path('validation/',views.validation,name="validation"),
    path('social_sign_in/', views.social_sign_in, name='social_sign_in'),
    path('reset/password/', views.ResetPasswordView.as_view(), name='reset_password'),

]
