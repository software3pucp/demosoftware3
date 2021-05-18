from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.core import serializers
from gestionarCurso.models import Curso
from gestionarEspecialidad.models import Especialidad
from gestionarFacultad.models import Facultad


def listarCursos(request):

    if request.POST:
        print('***************************************************************************************************')
        print(request)
        print('***************************************************************************************************')
        if request.POST['operacion'] == 'listEspe':
            especialidades = Especialidad.objects.filter(facultad_id=request.POST['facultad'])
            data = serializers.serialize("json", especialidades)
            return JsonResponse({"resp": data}, status=200)
        elif request.POST['operacion'] == 'listCur':
            cursos = Curso.objects.filter(especialidad_id=request.POST['especialidad'])
            data = serializers.serialize("json", cursos)
            return JsonResponse({"resp": data}, status=200)
    facultades = Facultad.objects.filter()
    especialidades = Especialidad.objects.filter()
    estados = ["Activo","Inactivo"]
    context = {
        'facultades' : facultades,
        'especialidades' : especialidades,
        'estados' : estados,
    }
    return render(request,'gestionarPlanMedicion/listarCursos.html',context)

def crearCursos(request,pk):
    insert = False
    flag = 0
    curso = Curso()
    curso.pk = pk
    especialidad = "Ingenieria Informática"
    listaCursos = Curso.objects.filter(especialidad_id = 1)
    listaHorarios = ["H0811","H0882","H0813","H0814"]
    listaEstados = ["Activo","Inactivo"]
    listaResponsables = ["Corrado Guillermo"]
    listaIndicadores = ["ID01","ID02","ID03"]

    if request.POST:
        if request.POST['operacion'] == 'entrada':
            # resultadoAcreditadora.acreditadora_id = request.POST["acreditadora"]
            flag=0

        elif request.POST['operacion'] == 'editar':
            # resultadoAcreditadora = ResultadoAcreditadora.objects.get(pk=pk)
            # resultadoAcreditadora.codigo = request.POST['codigo']
            # resultadoAcreditadora.descripcion = request.POST['descripcion']
            # resultadoAcreditadora.save()
            flag = 1

        elif request.POST['operacion'] == 'in   sertar':
            # ResultadoAcreditadora.objects.create(codigo=request.POST['codigo'],descripcion=request.POST['descripcion'],
            #                                      acreditadora_id=request.POST["acreditadora"])
            # resultadoAcreditadora = ResultadoAcreditadora.objects.latest('id')
            # pk = resultadoAcreditadora.pk
            flag = 2



    if pk == '0':
        insert = True
    else:
        curso = Especialidad.objects.get(pk=pk)

    context = {
        'especialidad' : especialidad,
        'listaCursos' : listaCursos,
        'listaHorarios':listaHorarios,
        'listaEstados':listaEstados,
        'listaResponsables':listaResponsables,
        'listaIndicadores': listaIndicadores,
        'curso' : curso,
        'insert': insert,
        'flag': flag,
    }
    return render(request,'gestionarPlanMedicion/crearCursos.html',context)


