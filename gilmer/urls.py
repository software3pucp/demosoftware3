

from django.urls import path, include

from gilmer import views

urlpatterns = [
    # path( 'URL A LA CUAL APUNTO', BACKEND, name= Nombre de la variable)
    path('home/', views.gilmerHome, name='gilmerHome'),
    path('pubgmTeam/insertar',views.insertarPubgmTeam,name='insertarPubgmTeam'),
    path('pubgmTeam/<pk>', views.detallePubgmTeam, name='detallePubgmTeam'),
    path('pubgmTeam/editar/<pk>',views.editarPubgmTeam,name='editarPubgmTeam'),
]
