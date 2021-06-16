from django.contrib.auth.models import Group
from django.shortcuts import render, redirect

# Create your views here.
from authentication.views import Show
from demosoftware3.settings import MEDIA_URL
from gestionarPlanMejora.models import EstadoActividad, PropuestaMejora, ActividadMejora, EvidenciaActividadMejora, \
    ResponsableMejora
from django.http import JsonResponse
from authentication.models import User


def crearActividad(request):  # quizas sea necesario pasar como parámetro el pk del plan de mejora
    estado = EstadoActividad.objects.get(pk=1)  # estado registrado
    propuestaMejora = PropuestaMejora.objects.get(pk=1)
    inicio = 2021  # año de inicio de la actividad
    fin = 2021  # año de fin de la actividad

    if request.POST:  # creación por metodo POST
        codigo = request.POST['codigo']
        descripcion = request.POST['descripcion']
        actividad = ActividadMejora.objects.create(codigo=codigo, descripcion=descripcion,
                                                   propuestaMejora=propuestaMejora, estado=estado,
                                                   inicio=inicio, fin=fin)
        responsables = request.POST.getlist('choices-multiple-remove-button')
        print(responsables)
        for val in responsables:
            user = User.objects.get(id=val)
            ResponsableMejora.objects.create(actividad=actividad, responsable=user)
        return redirect(Show)

    context = {
        'users': User.objects.all(),
        'grupos': Group.objects.all()

    }
    return render(request, 'gestionarPlanMejora/crearActividad.html', context)


def editarActividad(request, pk):
    media_path = MEDIA_URL
    if request.POST:
        actividad = ActividadMejora.objects.get(pk=pk)
        actividad.codigo = request.POST['codigo']
        actividad.descripcion = request.POST['descripcion']
        idEstado = request.POST['cboEstado']
        nuevoEstado = EstadoActividad.objects.get(pk=idEstado)
        actividad.estado = nuevoEstado
        actividad.save()
        # return redirect('') # regresa a la pagina anterior

    evidendia = EvidenciaActividadMejora.objects.get(pk=1)
    print('--------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print(media_path + evidendia.archivo.name)

    actividad = ActividadMejora.objects.get(pk=pk)
    estados = EstadoActividad.objects.filter()
    listaEvidencias = EvidenciaActividadMejora.objects.filter(actividad_id=pk, estado='1')
    responsables = ResponsableMejora.objects.filter(actividad_id=pk)
    print('--------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

    lresponsables = []
    for rs in responsables:
        lresponsables.append(User.objects.get(pk=rs.responsable_id))
    print(lresponsables)
    context = {
        'listaEvidencias': listaEvidencias,
        'actividad': actividad,
        'estados': estados,
        'media_path': media_path,
        'responsables': lresponsables,
        'users': User.objects.all(),
    }
    return render(request, 'gestionarPlanMejora/editarActividad.html', context)


def subirEvidencia(request, id_actividad):
    media_path = MEDIA_URL
    actividad = ActividadMejora.objects.get(pk=id_actividad)

    if request.POST:  # subir evidencia por método POST
        descripcion = request.POST['descripcion']
        concepto = request.POST['concepto']
        archivo = request.FILES['archivo']
        EvidenciaActividadMejora.objects.create(descripcion=descripcion, concepto=concepto,
                                                archivo=archivo, actividad=actividad)
        return redirect('editarActividad', pk=id_actividad)

    context = {
        'actividad': actividad,
        'media_path': media_path,
    }
    return render(request, 'gestionarPlanMejora/subirEvidencia.html', context)


def editarEvidencia(request, pk):
    media_path = MEDIA_URL
    if request.POST:
        descripcion = request.POST['descripcion']
        concepto = request.POST['concepto']
        archivo = request.FILES['archivo']

        evidencia = EvidenciaActividadMejora.objects.get(pk=pk)
        id_actividad = evidencia.actividad_id
        evidencia.descripcion = descripcion
        evidencia.concepto = concepto
        evidencia.archivo = archivo
        evidencia.save()
        return redirect('editarActividad', pk=id_actividad)

    evidencia = EvidenciaActividadMejora.objects.get(pk=pk)
    id_actividad = evidencia.actividad_id
    context = {
        'media_path': media_path,
        'evidencia': evidencia,
        'id_actividad': id_actividad,
    }
    return render(request, 'gestionarPlanMejora/editarEvidencia.html', context)


def eliminarEvidenciaxActividad(request):
    evidenciapk = request.POST['evidenciapk']
    evidencia = EvidenciaActividadMejora.objects.get(pk=evidenciapk)
    evidencia.estado = '0'
    evidencia.save()
    return JsonResponse({}, status=200)
