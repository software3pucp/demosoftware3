from django.db import models
from gestionarCurso.models import Curso
from gestionarSemestre.models import Semestre
from gestionarIndicadores.models import Indicador

# Create your models here.

class Alumno(models.Model):
    nombreAlumno = models.CharField(max_length=10, null=True, blank=True)
    codigoAlumno = models.CharField(max_length=9, null=True, blank=True)
    horario = models.CharField(max_length=5, null=True, blank=True)
    puntuacion = models.CharField(max_length=2,null=False,blank=True)

class MedicionDeIndicador(models.Model):
    codigo = models.CharField(max_length=10, default='', null=True, blank=True)
    resultado = models.CharField(max_length=4, default='', null=True, blank=True)
    semestre = models.ForeignKey(Semestre, on_delete=models.RESTRICT)
    curso = models.ForeignKey(Curso, on_delete=models.RESTRICT)
    alumno = models.ForeignKey(Alumno, on_delete=models.RESTRICT)


