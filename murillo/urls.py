from django.urls import path, include

from murillo import views

urlpatterns = [
    # path( 'URL A LA CUAL APUNTO', BACKEND, name= Nombre de la variable)
    path('home/',views.murilloHome,name='murilloHome'),
    path('pokemon/insertar',views.murilloInsertarPokemon,name='murilloInsertarPokemon'),
    path('pokemon/<pk>',views.murilloPokemonDetalle,name='murilloPokemonDetalle'),
    path('pokemon/editar/<pk>',views.murilloPokemonEditar,name='murilloPokemonEditar'),
]