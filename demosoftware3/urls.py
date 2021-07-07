"""demosoftware3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('home.urls')),
                  path('users/', include('authentication.urls')),
                  path('facultades/', include('gestionarFacultad.urls')),
                  path('especialidades/', include('gestionarEspecialidad.urls')),
                  path('cursos/', include('gestionarCurso.urls')),
                  path('horarios/', include('gestionarHorario.urls')),
                  path('gestionarAcreditadoras/', include('gestionarAcreditadoras.urls')),
                  path('gestionarREAcreditadoras/', include('gestionarREAcreditadoras.urls')),
                  path('gestionarSemestre/', include('gestionarSemestre.urls')),
                  path('gestionarNiveles/', include('gestionarNiveles.urls')),
                  path('gestionarResultados/', include('gestionarResultados.urls')),
                  path('gestionarResultadosMediciones/', include('gestionarResultadosMediciones.urls')),
                  path('gestionarEvaluacion/', include('gestionarEvaluacion.urls')),
                  path('gestionarPlanMedicion/', include('gestionarPlanMedicion.urls')),
                  path('gestionarIndicadores/', include('gestionarIndicadores.urls')),
                  path('gestionarEvidencia/', include('gestionarEvidencias.urls')),
                  path('gestionarHistoricoEv/', include('gestionarHistoricoEv.urls')),
                  path('gestionarPlanMejora/', include('gestionarPlanMejora.urls')),
                  path('gestionarObjetivosEducacionales/', include('gestionarObjetivosEducacionales.urls')),
                  path('accounts/', include('allauth.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
