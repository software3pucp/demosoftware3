import gestionarEspecialidad
from demosoftware3.settings import MEDIA_URL
from gestionarEspecialidad.models import Especialidad
from gestionarFacultad.models import Facultad
from gestionarCurso.models import Curso
from django.shortcuts import render, redirect
from authentication.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
# Create your views here.
from gestionarFacultad.views import listarFacultadxEsp, listarFacultad

@login_required
def listarEspecialidad(request):
    media_path = MEDIA_URL
    context = {
        'ListaEspecialidad': Especialidad.objects.filter(estado=Facultad.ESTADOS[1][0]),
        'ListaFacultad': Facultad.objects.all(),
        'media_path': media_path,
        'ListaEstados': Especialidad.ESTADOS[1:],
        'estado': '1',
    }
    return render(request, 'gestionarEspecialidad/listarEspecialidad.html', context)

@login_required
def listarEspecialidadDirector(request):
    media_path = MEDIA_URL
    user = User.objects.get(pk=request.user.pk)
    context = {
        'ListaEspecialidad': Especialidad.objects.filter(responsable=user.pk),
    }
    return render(request, 'gestionarEspecialidad/listarEspecialidadDirector.html',context)

@login_required
def listarEspecialidadxCurso(request, id_especialidad):
    print("==================================")
    print(id_especialidad)
    print("==================================")
    media_path = MEDIA_URL
    context = {
        'ListaCurso': Curso.objects.filter(especialidad_id=id_especialidad, estado=Especialidad.ESTADOS[1][0]),
        'ListaCursoInactivos': Curso.objects.filter(especialidad_id=id_especialidad, estado=Especialidad.ESTADOS[2][0]),
        'ListaEspecialidad': Especialidad.objects.all(),
        'id_especialidad': id_especialidad,
        'id_facultad': Especialidad.objects.get(pk=id_especialidad).facultad.pk,
        'media_path': media_path,
        'ListaEstados': Especialidad.ESTADOS[1:],
        'estado':'1'
    }
    return render(request, 'gestionarCurso/listarCurso.html', context)

@login_required
def agregarEspecialidad(request, id_facultad):
    media_path = MEDIA_URL
    if request.POST:
        if ('name' in request.POST):
            nombre = request.POST['name']
            id_responsable = request.POST['responsable']
            foto = request.FILES['photo']
            facultad = Facultad.objects.get(pk=id_facultad)
            Especialidad.objects.create(nombre=nombre, responsable=id_responsable, facultad=facultad, foto=foto,
                                        estado=request.POST['estado'])

            #Si el usuario no tiene rol de cooordinador de especialidad se lo agrego
            user = User.objects.get(pk=id_responsable)
            group = Group.objects.get(name="Coordinador de especialidad")
            userGroup = list(User.groups.through.objects.filter(user_id=id_responsable,group_id=group.pk))
            if len(userGroup) == 0:
                group.user_set.add(user)
                user.n_Roles = user.n_Roles + 1
                user.save()
            return redirect('listarFacultadxEsp',id_facultad)

    context = {
        'ListaUsuarios': User.objects.all(),
        'ListaFacultad': Facultad.objects.all(),
        'id_facultad': id_facultad,
        'media_path': media_path,
        'estado': request.POST["estado"]
    }
    return render(request, 'gestionarEspecialidad/agregarEspecialidad.html', context)

@login_required
def editarEspecialidad(request, id_especialidad):
    media_path = MEDIA_URL
    especialidad = Especialidad.objects.get(pk=id_especialidad)
    id_facultad = Facultad.objects.get(pk=especialidad.facultad_id).pk
    estado = especialidad.estado
    if request.POST:
        print(request.POST)
        group = Group.objects.get(name="Coordinador de especialidad")

        # Quitar rol de coordinador de especialidad a responsable si es necesario
        responsable = User.objects.get(pk=especialidad.responsable)
        especialidades = list(Especialidad.objects.filter(responsable=responsable.pk))
        if len(especialidades) == 1:
            group.user_set.remove(responsable)
            responsable.n_Roles = responsable.n_Roles - 1
            responsable.save()

        nuevo_nombre = request.POST["name"]
        nuevo_responsable = request.POST["responsable"]
        if request.FILES.get('photo'):
            nueva_foto = request.FILES["photo"]
            especialidad.foto = nueva_foto
        especialidad.nombre = nuevo_nombre
        especialidad.responsable = nuevo_responsable
        especialidad.save()

        #Agregar rol de coordinador de especialidad a nuevo responsable si no lo tiene
        user = User.objects.get(pk=nuevo_responsable)
        userGroup = list(User.groups.through.objects.filter(user_id=nuevo_responsable, group_id=group.pk))
        if len(userGroup) == 0:
            group.user_set.add(user)
            user.n_Roles = user.n_Roles + 1
            user.save()

        return redirect('listarFacultadxEsp', id_facultad)

    context = {
        'media_path': media_path,
        'especialidad': especialidad,
        'id_responsable': especialidad.responsable,
        'ListaUsuarios': User.objects.all()
    }
    return render(request, 'gestionarEspecialidad/editarEspecialidad.html', context)

@login_required
def eliminarEspecialidad(request, id_especialidad):
    especialidad = Especialidad.objects.get(pk=id_especialidad)
    fakuPK = especialidad.facultad.pk
    especialidad.delete()
    return redirect('listarFacultadxEsp', fakuPK)

@login_required
def eliminarEspecialidad2(request, id_especialidad):
    especialidad = Especialidad.objects.get(pk=id_especialidad)
    estado = especialidad.estado
    id_facultad = Facultad.objects.get(pk=especialidad.facultad_id).pk
    fakuPK = especialidad.facultad.pk
    media_path = MEDIA_URL
    if especialidad.estado == Especialidad.ESTADOS[2][0]:
        especialidad.estado = Especialidad.ESTADOS[1][0]
    elif especialidad.estado == Especialidad.ESTADOS[1][0]:
        especialidad.estado = Especialidad.ESTADOS[2][0]
    especialidad.save()
    return redirect('listarFacultadxEsp', id_facultad)

