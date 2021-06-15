from django.db import models

# Create your models here.
from gestionarCurso.models import Curso
from gestionarHorario.models import Horario
from gestionarIndicadores.models import Indicador
from gestionarSemestre.models import Semestre


class PlanMedicion(models.Model):
    ESTADOS = [
        ('0', 'Eliminado'),
        ('1', 'Activo'),
    ]
    nombre = models.CharField(max_length=100)
    semestre = models.ManyToManyField(Semestre)
    estado = models.CharField(max_length=2, choices=ESTADOS, default=None, null=True, blank=True)


class PlanMedicionCurso(models.Model):
    ESTADOS = [
        ('0', 'Eliminado'),
        ('1', 'Activo'),
        ('2', 'Inactivo'),
    ]
    curso = models.ForeignKey(Curso, on_delete=models.RESTRICT)
    indicador = models.ManyToManyField(Indicador)
    horario = models.ManyToManyField(Horario)
    planMedicion = models.ForeignKey(PlanMedicion, on_delete=models.RESTRICT)
    semestre = models.ForeignKey(Semestre, on_delete=models.RESTRICT)
    estado = models.CharField(max_length=2, choices=ESTADOS, default=None, null=True, blank=True)
