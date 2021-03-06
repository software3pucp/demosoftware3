from django.urls import path, include

from gestionarREAcreditadoras import views

urlpatterns = [
    # path( url hijo, backend, nombre de la variable)
    path('listar/<pk>', views.listarRE, name="listarRE"),
    path('editar/<pk>', views.editarRE, name="editarRE"),
    path('ajaxEditar', views.ajaxEditar, name="ajaxEditar"),
    path('activarREA/', views.activarREA, name="activarREA"),
    path('desactivarREA/', views.desactivarREA, name="desactivarREA"),
    path('listarREA/', views.listarREA, name="listarREA"),
]