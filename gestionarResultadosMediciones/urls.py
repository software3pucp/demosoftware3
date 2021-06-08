from django.urls import path, include

from gestionarResultadosMediciones import views

urlpatterns = [
    path('resultados/', views.resultadosMediciones, name="resultadosMediciones"),
]