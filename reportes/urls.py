from django.urls import path, include

from reportes import views

urlpatterns = [
    path('reportes/', views.reportes, name="reportes"),
    path('filtrarEspecialidades/', views.obtenerEspecialidades, name="filtrarEspecialidades"),

]
