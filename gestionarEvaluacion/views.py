from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from openpyxl import Workbook,load_workbook,styles
import os
from django.conf import settings
# Create your views here.
from demosoftware3.settings import MEDIA_URL
from gestionarEvaluacion.models import RespuestaEvaluacion
from gestionarHorario.models import Horario
from gestionarEspecialidad.models import Especialidad
from gestionarIndicadores.models import Indicador
from gestionarRubrica.models import Rubrica
from gestionarEvidencias.models import EvidenciasxHorario
from gestionarNiveles.models import Nivel
from gestionarCurso.models import Curso
from authentication.models import User
from gestionarResultados.models import ResultadoPUCP
from gestionarPlanMedicion.models import PlanMedicionCurso
from django.contrib.auth.decorators import login_required
# import xlrd libreria para importar Alumnos
@login_required
def evaluar(request,pk):
    media_path = MEDIA_URL
    listaAlumno = reversed(RespuestaEvaluacion.objects.filter(estado=1))
    cursoSeleccionado = Curso.objects.get(pk=pk)
    plan = PlanMedicionCurso.objects.get(curso=cursoSeleccionado)
    horarios = plan.horario.all()
   # listaHorario= Horario.objects.filter(curso_id=pk) #listaDeHorario asociado a un curso
    especialidadPk = cursoSeleccionado.especialidad_id
    resultado = list(ResultadoPUCP.objects.filter(especialidad_id=especialidadPk))

    if resultado:
        indicadores = plan.indicador.all()
        listaIndicador = list(indicadores)
        #listaIndicador = Indicador.objects.filter(resultado_id=resultado[0].id ,estado=1)
    else:
        listaIndicador = []
    listaHorarios = list(horarios)
    #listaHorarios = list(Horario.objects.filter(curso_id=pk, estado=1))
    # listaDocumentos = EvidenciasxHorario.objects.filter(estado=1)
    listaDocumentos = EvidenciasxHorario.objects.none()
    listaNombres = []
    for i in range(len(listaHorarios)):
        listaEDocumentos = EvidenciasxHorario.objects.filter(horario_id=listaHorarios[i].id, estado=1)
        if listaEDocumentos:
            aux = list(listaEDocumentos)
            for j in range(len(aux)):
                nombArchivo = str(aux[j].archivo)[8:]
                listaNombres.append(nombArchivo)
            # listaEDocumentos.update(archivo=nombArchivo)
            listaDocumentos = listaDocumentos | listaEDocumentos
    cantidad = len(listaNombres)
    listaConjunta = zip(listaNombres, listaDocumentos)
    listaArchivos = set(listaConjunta)

    context = {
        'media_path': media_path,
        'listaAlumno': listaAlumno,
        'listaIndicador': listaIndicador,
        'cursoSeleccionado': cursoSeleccionado,
        'listaHorario': listaHorarios,
        'listaDocumentos': listaDocumentos,
        'listaNombres': listaNombres,
        'cantidad': cantidad,
        'users': User.objects.all(),
        'listaAux': listaArchivos,
    }
    return render(request, 'gestionarEvaluacion/baseEvaluacion/base.html',context)

def agregarAlumno(request):
    print(request.POST)
    niveles = Nivel.objects.filter(estado="1")
    nuevoAlumno = RespuestaEvaluacion.objects.create(nombreAlumno=request.POST["nombreAlumno"],
                                                     codigoAlumno=request.POST["codigoAlumno"],
                                                     horario_id=request.POST["horario"],
                                                     indicador_id=request.POST["indicador"])
    ser_instance = serializers.serialize('json', [nuevoAlumno,])
    ser_instance2 = serializers.serialize('json', list(niveles), fields=('id', 'nombre', 'valor', 'estado'))
    return JsonResponse({"nuevoAlumno": ser_instance,"niveles": ser_instance2 }, status=200)

def guardarPuntuacion(request):
    alumno = RespuestaEvaluacion.objects.get(pk=request.POST["idAlumno"])
    descripcion = Rubrica.objects.get(indicador_id=request.POST["indicadorSeleccionado"],nivel_id=request.POST["nivelSeleccionado"]).descripcion
    alumno.descripcionP = descripcion
    alumno.valorNota = Nivel.objects.get(pk=request.POST["nivelSeleccionado"]).valor
    alumno.rubrica_id = Rubrica.objects.get(indicador_id=request.POST["indicadorSeleccionado"],nivel_id=request.POST["nivelSeleccionado"]).pk
    alumno.calificado = 1
    alumno.save()
    return JsonResponse({},status=200)

def editarAlumno(request):
    alumno = RespuestaEvaluacion.objects.get(pk = request.POST["idAlumno"])
    nuevoCodigo = request.POST["codigoAlumno"]
    nuevoNombre = request.POST["nombreAlumno"]
    alumno.codigoAlumno = nuevoCodigo
    alumno.nombreAlumno = nuevoNombre
    alumno.save()
    return JsonResponse({}, status=200)

def eliminarAlumno(request):
    alumno = RespuestaEvaluacion.objects.get(pk = request.POST["idAlumno"])
    alumno.estado = 0
    alumno.save()
    return JsonResponse({}, status=200)

def muestraRubrica(request):
    niveles = Nivel.objects.filter(estado="1")
    rubrica = Rubrica.objects.filter(indicador_id=request.POST["indicadorSeleccionado"])
    indicador = Indicador.objects.get(pk=request.POST["indicadorSeleccionado"])
    ser_instance = serializers.serialize('json', list(rubrica),fields=('id','descripcion','especialidad','indicador','nivel'))
    ser_instance2 = serializers.serialize('json',[indicador,])
    ser_instance3 = serializers.serialize('json', list(niveles),fields=('id','nombre','valor','estado'))
    return JsonResponse({"rubrica": ser_instance,"indicador":ser_instance2, "niveles": ser_instance3 }, status=200)

def listarAlumno(request):
    filtrado = request.POST["filtrado"]
    especialidad = Especialidad.objects.get(pk=request.POST["especialidadSeleccionada"])
    niveles = Nivel.objects.filter(estado="1",especialidad_id=especialidad.pk)
    if (filtrado!=""):
        if (filtrado.isnumeric()):
            listaAlumno = reversed(RespuestaEvaluacion.objects.filter(codigoAlumno__contains=filtrado, horario_id = request.POST["horarioSeleccionado"],indicador_id=request.POST["indicadorSeleccionado"], estado=1))
        else:
            listaAlumno = reversed(RespuestaEvaluacion.objects.filter(nombreAlumno__contains=filtrado, horario_id=request.POST["horarioSeleccionado"],indicador_id=request.POST["indicadorSeleccionado"], estado=1))
    else:
        listaAlumno = reversed(RespuestaEvaluacion.objects.filter(horario_id=request.POST["horarioSeleccionado"],indicador_id=request.POST["indicadorSeleccionado"], estado=1))

    ser_instance = serializers.serialize('json', list(listaAlumno),fields=('id', 'nombreAlumno', 'codigoAlumno', 'horario','calificado', 'valorNota','evidencia'))
    ser_instance2 = serializers.serialize('json', list(niveles), fields=('id', 'nombre', 'valor', 'estado'))
    return JsonResponse({"listaAlumno": ser_instance, "niveles": ser_instance2},  status=200)

def importarAlumno(request):
    # Funciona si guardas de nuevo el archivo descargado mediante campus porque dice que en este el formato y la
    # extension no coinciden, si se vuelve a guardar el archivo como xls si se puede guardar
    # wb = xlrd.open_workbook(filename=None, file_contents=request.FILES['archivo'].read())
    # table = wb.sheets()[0]
    # row = table.nrows
    # for i in range(7, row):
    #     col = table.row_values(i)
    #     if (col[0] == ''):
    #         break
    #     else:
    #         RespuestaEvaluacion.objects.create(nombreAlumno=col[1], codigoAlumno=int(col[0]),
    #                                                horario_id=request.POST["horariopk"])
    # return JsonResponse({}, status=200)
    excel = request.FILES['archivo']
    rows = excel.read().decode().split('\n')
    for row in rows:
        codigo = row[:8]
        nombre = row[9:-1]
        if(codigo!=""):
            RespuestaEvaluacion.objects.create(nombreAlumno=nombre,codigoAlumno=codigo,horario_id=request.POST["horariopk"], indicador_id=request.POST["indicador"])
    return JsonResponse({}, status=200)

def subirEvidencia(request):
    # TODO::: Subir archivo a BBDD del PK del Evaluado
    print(request.POST["evaluadopk"])
    alumno = RespuestaEvaluacion.objects.get(pk=request.POST["evaluadopk"])
    # TODO::: Agregar una columna para guardar la evidencia
    alumno.evidencia = 1
    alumno.archivo = request.FILES["archivo"]
    alumno.save()
    # TODO::: Mandar una respuesta adecuada al front (Se hace con un IF y en dos JSONRESPONSE
    print(request.FILES["archivo"])
    return JsonResponse({}, status=200)


def exportarMedicion(request):
    horarioSeleccionado = request.POST['cboHorario']
    indicadorSeleccionado = Indicador.objects.get(pk=request.POST['cboIndicador'])
    resultadoAsociado = ResultadoPUCP.objects.get(pk=indicadorSeleccionado.resultado.pk)
    curso = Curso.objects.get(id=Horario.objects.get(id=horarioSeleccionado).curso_id)

    #Apertura de template.xlsx
    filename = os.path.join(settings.BASE_DIR, 'gestionarEvaluacion', 'Resource', 'template.xlsx')
    wb = load_workbook(filename)
    ws= wb.active

    #CABECERAS
    ws['E3'] = f'MEDICIÓN DEL CURSO -  {curso.nombre.upper()}'
    ws['D5'] = curso.nombre.upper()
    ws['G5'] = Horario.objects.get(id=horarioSeleccionado).codigo
    ws['D7'] = User.objects.get(id = Horario.objects.get(id=horarioSeleccionado).responsable).first_name
    ws['E15']= ws['E24'] =  f'{indicadorSeleccionado.codigo}\n{indicadorSeleccionado.descripcion}'
    ws['E14']= ws['E23'] =  f'{resultadoAsociado.codigo} - {resultadoAsociado.descripcion}'

    #Impresion de Puntajes
    rows = RespuestaEvaluacion.objects.filter(horario_id=horarioSeleccionado,estado="1")
    i = 0
    for row in rows:
        ws[f'B{25 + i}'] = i + 1
        ws[f'C{25 + i}'] = row.codigoAlumno
        ws[f'D{25 + i}'] = row.nombreAlumno
        ws[f'E{25 + i}'] = row.valorNota if row.valorNota != None else 0
        i+=1

    #Resultados
    niveles = Nivel.objects.filter(especialidad_id=curso.especialidad_id, estado='1').order_by('-valor')
    valorMax = niveles[0].valor
    ws['E18'] = i
    if i>0:
        ws['E16'] = f'=SUMA(E25:H{25+i-1})/{i}'
        ws['E17'] = f'=SUMA(E25:H{25 + i - 1})/{i}/{valorMax}*100%'


    #Establecer el nombre del archivo
    nombre_archivo = "Reporte.xlsx"

    #Definir el tipo de respuesta que se va a dar
    response= HttpResponse(content_type="application/ms-excel")
    contenido = "attachment; filename = {0}".format(nombre_archivo)
    response["Content-Disposition"] = contenido
    wb.save(response)
    return response