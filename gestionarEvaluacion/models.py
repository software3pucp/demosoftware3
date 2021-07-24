from django.db import models
from gestionarCurso.models import Curso
from gestionarSemestre.models import Semestre
from gestionarIndicadores.models import Indicador
from gestionarHorario.models import Horario
from gestionarRubrica.models import Rubrica
from gestionarPlanMedicion.models import PlanMedicionCurso

# Create your models here.

class RespuestaEvaluacion(models.Model):
    nombreAlumno = models.CharField(max_length=10, null=True, blank=True)
    codigoAlumno = models.CharField(max_length=9, null=True, blank=True)
    horario = models.ForeignKey(Horario, on_delete=models.RESTRICT, null=True, blank=True)
    descripcionP = models.CharField(max_length=200,null=False,blank=True)
    valorNota = models.IntegerField(null=True)
    rubrica = models.ForeignKey(Rubrica,on_delete=models.RESTRICT, null=True, blank=True)
    indicador = models.ForeignKey(Indicador,on_delete=models.RESTRICT, null=True, blank=True)
    estado = models.CharField(max_length=2,default=1)
    calificado = models.CharField(max_length=2,null=True, default=0)
    planMedicion = models.ForeignKey(PlanMedicionCurso,on_delete=models.RESTRICT, null=True, blank=True)
    evidencia = models.CharField(max_length=2, null=True, default=0)
    archivo = models.FileField(null=True, blank=True, upload_to='archive/')
    class Meta:
        ordering = ['codigoAlumno']

class MedicionDeIndicador(models.Model):
    codigo = models.CharField(max_length=10, default='', null=True, blank=True)
    resultado = models.CharField(max_length=4, default='', null=True, blank=True)
    semestre = models.ForeignKey(Semestre, on_delete=models.RESTRICT,null=True, blank=True)
    curso = models.ForeignKey(Curso, on_delete=models.RESTRICT,null=True, blank=True)
    alumno = models.ForeignKey(RespuestaEvaluacion, on_delete=models.RESTRICT,null=True,blank=True)

    class Meta:
        ordering = ['codigo']

