from django.contrib.auth.models import Group

from demosoftware3.settings import MEDIA_URL
from gestionarFacultad.models import Facultad
from django.shortcuts import render, redirect
from authentication.models import User, User_Groups_Extended
from django.contrib.auth.decorators import login_required
from gestionarEspecialidad.models import Especialidad
from gestionarFacultad.models import Facultad
from django.shortcuts import render, redirect
from authentication.models import User


@login_required
# Create your views here.
def listarFacultad(request):
    # print(request.user.rol_actual)

    if (request.user.rol_actual == 'Coordinador de facultad'):
        usuario = request.user
        grupo = Group.objects.get(name="Coordinador de facultad")

        print(usuario)
        print(grupo)

        usuario_grupo = User.groups.through.objects.get(user_id=usuario.pk, group_id=grupo.pk)
        print(usuario_grupo.id)
        print(usuario_grupo.user_id)
        print(usuario_grupo.group_id)
        registros = User_Groups_Extended.objects.filter(userGroup=usuario_grupo.id)

        facultades=[]
        for item in registros:
            facultad = Facultad.objects.get(pk=item.facultad.pk)
            facultades.append(facultad)

        media_path = MEDIA_URL
        context = {
            'ListaFacultad':facultades,
            'media_path': media_path,
        }
        return render(request, 'gestionarFacultad/listarFacultadCoordinador.html', context)


    media_path = MEDIA_URL
    context = {
        'ListaFacultad': Facultad.objects.filter(estado=Facultad.ESTADOS[1][0]),
        'ListaFacultadInactivos': Facultad.objects.filter(estado=Facultad.ESTADOS[2][0]),
        'ListaEstados': Facultad.ESTADOS[1:],
        'media_path': media_path,
        'estado': '1'
    }
    return render(request, 'gestionarFacultad/listarFacultad.html', context)


@login_required
def agregarFacultad(request):
    media_path = MEDIA_URL
    if request.POST:
        if ('name' in request.POST):
            nombre = request.POST['name']
            id_responsable = request.POST['responsable']
            foto = request.FILES['photo']
            Facultad.objects.create(nombre=nombre, responsable=id_responsable, foto=foto, estado=request.POST["estado"])
            return redirect(listarFacultad)
        else:
            context = {
                'ListaUsuarios': User.objects.all(),
                'estado': request.POST['estado'],
            }
            return render(request, 'gestionarFacultad/agregarFacultad.html', context)
    context = {
        'ListaUsuarios': User.objects.all(),
    }
    return render(request, 'gestionarFacultad/agregarFacultad.html', context)


@login_required
def listarFacultadxEsp(request, id_facultad):
    media_path = MEDIA_URL
    context = {
        'ListaEspecialidad': Especialidad.objects.filter(facultad_id=id_facultad, estado=Facultad.ESTADOS[1][0]),
        'ListaEspecialidadInactivos': Especialidad.objects.filter(facultad_id=id_facultad,
                                                                  estado=Facultad.ESTADOS[2][0]),
        'ListaFacultad': Facultad.objects.all(),
        'id_facultad': id_facultad,
        'media_path': media_path,
        'ListaEstados': Especialidad.ESTADOS[1:],
        'estado': '1'
    }
    return render(request, 'gestionarEspecialidad/listarEspecialidad.html', context)


@login_required
def editarFacultad(request, id_facultad):
    ListaUsuarios = User.objects.filter()
    media_path = MEDIA_URL
    facultad = Facultad.objects.get(pk=id_facultad)
    if request.POST:
        nuevo_nombre = request.POST["name"]
        nuevo_responsable = request.POST["responsable"]
        if request.FILES.get('photo'):
            nueva_foto = request.FILES["photo"]
            facultad.foto = nueva_foto
        facultad.nombre = nuevo_nombre
        facultad.responsable = nuevo_responsable
        facultad.save()
        return redirect('listarFacultad')

    context = {
        'facultad': facultad,
        'media_path': media_path,
        'ListaUsuarios': ListaUsuarios,
        'id_responsable': facultad.responsable,
    }
    return render(request, 'gestionarFacultad/editarFacultad.html', context)


@login_required
def eliminarFacultad(request, id_facultad):
    media_path = MEDIA_URL
    facultad = Facultad.objects.get(pk=id_facultad)
    context = {
        'ListaFacultad': Facultad.objects.filter(estado=Facultad.ESTADOS[1][0]),
        'ListaFacultadInactivos': Facultad.objects.filter(estado=Facultad.ESTADOS[2][0]),
        'ListaEstados': Facultad.ESTADOS[1:],
        'media_path': media_path,
        'estado': facultad.estado,
    }
    facultad.delete()
    print("Correcto eliminar Facultad!")
    return render(request, 'gestionarFacultad/listarFacultad.html', context)


@login_required
def eliminarFacultad2(request, id_facultad):
    media_path = MEDIA_URL
    facultad = Facultad.objects.get(pk=id_facultad)
    if facultad.estado == Facultad.ESTADOS[2][0]:
        facultad.estado = Facultad.ESTADOS[1][0]
    elif facultad.estado == Facultad.ESTADOS[1][0]:
        facultad.estado = Facultad.ESTADOS[2][0]
    facultad.save()
    print("Correcto desactivar Facultad!")
    return redirect('listarFacultad')
