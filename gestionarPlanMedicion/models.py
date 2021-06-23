from django.db import models

# Create your models here.
from gestionarCurso.models import Curso
from gestionarEspecialidad.models import Especialidad
from gestionarIndicadores.models import Indicador
from gestionarResultados.models import PlanResultados
from gestionarSemestre.models import Semestre


class PlanMedicion(models.Model):
    ESTADOS = [
        ('0', 'Eliminado'),
        ('1', 'Activo'),
        ('2', 'Terminado'),
    ]
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    semestre = models.ManyToManyField(Semestre)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.RESTRICT)
    planResultados = models.ForeignKey(PlanResultados, on_delete=models.RESTRICT)
    estado = models.CharField(max_length=2, choices=ESTADOS, default=None, null=True, blank=True)

class PlanMedicionCurso(models.Model):
    ESTADOS = [
        ('0', 'Eliminado'),
        ('1', 'Activo'),
        ('2', 'Inactivo'),
    ]
    curso = models.ForeignKey(Curso, on_delete=models.RESTRICT)
    indicador = models.ManyToManyField(Indicador)
    planMedicion = models.ForeignKey(PlanMedicion, on_delete=models.RESTRICT)
    semestre = models.ForeignKey(Semestre, on_delete=models.RESTRICT)
    estado = models.CharField(max_length=2, choices=ESTADOS, default=None, null=True, blank=True)
