from django.db import models

# Create your models here.
from gestionarCurso.models import Curso
from gestionarIndicadores.models import Indicador


class PlanMedicion(models.Model):
    ESTADOS = [
        ('0', 'Eliminado'),
        ('1', 'Activo'),
        ('2', 'Inactivo'),
    ]
    curso = models.ForeignKey(Curso,on_delete=models.RESTRICT)
    indicador = models.ManyToManyField(Indicador)
    estado = models.CharField(max_length=2, choices=ESTADOS, default=None, null=True, blank=True)
