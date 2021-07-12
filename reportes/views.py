from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
# Create your views here.
from gestionarEspecialidad.models import Asistente, Auditor, Especialidad
from django.contrib.auth.models import Group

from gestionarFacultad.models import Facultad
from gestionarSemestre.models import Semestre
import os
from openpyxl import Workbook,load_workbook,styles
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from validate_email import validate_email
from django.urls import reverse
from django.views.generic import FormView
from authentication.forms import ChangePasswordForm
from django.http import HttpResponseRedirect
from authentication.models import User
from demosoftware3.settings import MEDIA_URL
from gestionarFacultad.views import listarFacultad
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.models import Group
from demosoftware3 import settings
import uuid
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.template.loader import render_to_string
import pandas as pd
import math

from gestionarIndicadores.models import Indicador
from gestionarPlanMedicion.models import PlanMedicion, PlanMedicionCurso
from gestionarResultados.models import ResultadoPUCP, PlanResultados

from gestionarSemestre.models import Semestre

from gestionarHorario.models import Horario

from gestionarEvaluacion.models import RespuestaEvaluacion

from gestionarNiveles.models import Nivel



from gestionarEspecialidad.models import Especialidad

from gestionarRubrica.models import Rubrica



@login_required
def reportes(request):
    especialidades = []
    facultades = []
    semestres = Semestre.objects.filter()

    if (request.user.rol_actual == "Asistente de acreditación"):
        usuario = request.user
        especialidades = []
        items = Asistente.objects.filter(user_id=usuario.pk)
        for item in items:
            especialidades.append(item.especialidad)
        context = {
            'semestres':semestres,
            'especialidades': especialidades,
        }
        return render(request, 'reportes/reportesCE.html', context)

    if (request.user.rol_actual == "Auditor"):
        usuario = request.user
        especialidades = []
        items = Auditor.objects.filter(user_id=usuario.pk)
        for item in items:
            especialidades.append(item.especialidad)
        context = {
            'semestres': semestres,
            'especialidades': especialidades,
        }
        return render(request, 'reportes/reportesCE.html', context)

    if (request.user.rol_actual == "Coordinador de facultad"):
        usuario = request.user
        grupo = Group.objects.get(pk=4)
        facultades = Facultad.objects.filter(responsable=usuario.pk)
        context = {
            'semestres': semestres,
            'facultades': facultades,
        }
        return render(request, 'reportes/reportesCF.html', context)

    if (request.user.rol_actual == "Coordinador de especialidad"):
        usuario = request.user
        grupo = Group.objects.get(pk=5)
        especialidades = Especialidad.objects.filter(responsable=usuario.pk)
        context = {
            'semestres': semestres,
            'especialidades': especialidades,
        }
        return render(request, 'reportes/reportesCE.html', context)

def obtenerEspecialidades(request):
    id_facultad = request.POST['facultad']
    especialidades = Especialidad.objects.filter(facultad_id=id_facultad, estado='1')
    data = serializers.serialize("json", especialidades)
    return JsonResponse({"resp": data}, status=200)

def generarReportes(request):
    if request.POST:

        esp = request.POST['cboEspecialidad']
        ciclo = request.POST['cboSemestre']
        print("esp", esp)
        print("ciclo", ciclo)

        if '_rubricas' in request.POST:
            print("rubricas")
            #Apertura de template.xlsx
            filename = os.path.join(settings.BASE_DIR, 'reportes', 'Resources', 'template.xlsx')
            wb = load_workbook(filename)
            ws = wb.active

            nivelesX = []
            nivelesY=[]
            especialidad = Especialidad.objects.get(pk=esp)
            niveles = Nivel.objects.filter(especialidad_id=esp,estado='1')
            for n in range(len(niveles)):
                if n == 0:
                    nivelesX.append('D')
                    nivelesY.append('B')
                else:
                    nivelesX.append(chr(ord(nivelesX[n - 1]) + 1))
                ws[f'{nivelesX[n]}7'] = f'{niveles[n].nombre} ({niveles[n].valor})'
                currentcell = ws[f'{nivelesX[n]}7']
                currentcell.font = Font(name='Calibri', size=11, bold="True")
                currentcell.alignment = Alignment(horizontal='center', vertical='center', wrapText=True)
                currentcell.fill = PatternFill(start_color="C0C0C0", end_color="C0C0C0", fill_type="solid")
                if n == 0:
                    currentcell.border = Border(left=Side(border_style='thin'), top=Side(border_style='thin'),
                                                bottom=Side(border_style='thin'))
                elif n == len(niveles) - 1:
                    currentcell.border = Border(right=Side(border_style='thin'), top=Side(border_style='thin'),
                                                bottom=Side(border_style='thin'))
                else:
                    currentcell.border = Border(top=Side(border_style='thin'), bottom=Side(border_style='thin'))

            ws.merge_cells(f'D6:{nivelesX[len(niveles) - 1]}6')
            ws.merge_cells(f'B5:{nivelesX[len(niveles) - 1]}5')

            ws['C3'] = f'RÚBRICAS DEL PROGRAMA DE {especialidad.nombre.upper()}'

            semAux = Semestre.objects.get(pk=ciclo)
            planSemestre = PlanMedicion.semestre.through.objects.filter(semestre_id=semAux.pk)
            planCal = None
            for p in planSemestre:
                estado = [1, 2]
                planesMedi = PlanMedicion.objects.filter(pk=p.planmedicion_id, estado__in=estado, especialidad_id=esp)
                if planesMedi:
                    planCal = planesMedi[0]
                    break

            plResultado = PlanResultados.objects.filter(pk=planCal.planResultados.pk)
            if plResultado:
                for plR in plResultado:
                    resTodos = ResultadoPUCP.objects.filter(planResultado_id=plR.pk, estado=1)
                    for i in range(len(resTodos)):
                        res = resTodos[i]
                        codResul = res.codigo
                        ws.title = codResul
                        if i < len(resTodos) - 1:
                            wb.copy_worksheet(ws)
                            nombreAux = codResul + " Copy"
                            ws = wb[nombreAux]

                        wsAux = wb[codResul]
                        wsAux['B5'] = f'{res.codigo} ({res.descripcion})'
                        wsAux['B5'].alignment = Alignment(horizontal='center', vertical='center', wrapText=True)
                        filaInicio = 8
                        indImpr = Indicador.objects.filter(resultado_id=resTodos[i].pk, estado=1)
                        if indImpr:
                            for numInd in range(len(indImpr)):
                                wsAux[f'C{filaInicio}'] = f'{indImpr[numInd].codigo} {indImpr[numInd].descripcion}'
                                celdaEstilo = wsAux[f'C{filaInicio}']
                                celdaEstilo.alignment = Alignment(horizontal='left', vertical='center', wrapText=True)
                                celdaEstilo.border = Border(left=Side(border_style='thin'), top=Side(border_style='thin'),
                                                            bottom=Side(border_style='thin'))
                                celdaEstilo.font = Font(name='Calibri', size=12, bold="True")
                                for n in range(len(niveles)):
                                    rubrica = Rubrica.objects.filter(indicador_id=indImpr[numInd].pk,
                                                                     nivel_id=niveles[n].pk)
                                    if rubrica:
                                        wsAux[f'{nivelesX[n]}{filaInicio}'] = rubrica[0].descripcion
                                    rubricaEstilo = wsAux[f'{nivelesX[n]}{filaInicio}']
                                    rubricaEstilo.alignment = Alignment(horizontal='left', vertical='center', wrapText=True)
                                    rubricaEstilo.font = Font(name='Calibri', size=11, bold=False)
                                    if n == len(niveles) - 1:
                                        rubricaEstilo.border = Border(left=None,
                                                                      right=Side(border_style='thin'),
                                                                      top=Side(border_style='thin'),
                                                                      bottom=Side(border_style='thin'))
                                    else:
                                        rubricaEstilo.border = Border(left=None,
                                                                      right=None,
                                                                      top=Side(border_style='thin'),
                                                                      bottom=Side(border_style='thin'))
                                filaInicio += 1
                        if filaInicio > 8:
                            wsAux.merge_cells(f'B8:B{filaInicio - 1}')

            nom_arch = f'Rubrica {especialidad.nombre}.xlsx'
            # Definir el tipo de respuesta que se va a dar
            response = HttpResponse(content_type="application/ms-excel")
            contenido = "attachment; filename = {0}".format(nom_arch)
            response["Content-Disposition"] = contenido
            wb.save(response)
            return response
        elif '_resultados' in request.POST:
            print("resultados")
    return render(request, 'reportes/reportesCE.html')