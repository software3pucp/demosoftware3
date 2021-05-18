#ESTOS SON LOS URLS DEL MÓDULO
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import  LoginView,LogoutView
from authentication import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)
    path('login/',LoginView.as_view(template_name='authentication/login.html'), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('add/', views.Register, name='user'),
    path('',views.Show, name='showUsers'),
    path('edit/<pk>', views.Edit, name='editUsers'),
    path('del/<pk>', views.Delete, name='deleteUser')
]
