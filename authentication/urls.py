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
    path('activate/<pk>', views.Activate, name='activateUser'),
    path('select_rol/',views.select_rol, name="selectrol"),
    path('validation/',views.validation,name="validation"),
    path('social_sign_in/', views.social_sign_in, name='social_sign_in'),
    path('reset/password/', views.renderForgotPassword, name='forgotPassword'),
    path('forgotPassword', views.ResetPassword, name='reset_password'),
    path('change/password/<str:token>/', views.ChangePasswordView.as_view(), name='renderChangePassword'),
    path('changePassword/<pk>/',views.changePassword,name='changePassword'),
    path('importarUsuarios/',views.importarUsuarios,name='importarUsuarios'),

]
