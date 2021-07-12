from django.urls import path, include

from reportes import views

urlpatterns = [
    path('', views.reportes, name="reportes"),
    path('filtrarEspecialidades/', views.obtenerEspecialidades, name="filtrarEspecialidades"),
    path('reportes/',views.generarReportes, name="generarReportes")
]
