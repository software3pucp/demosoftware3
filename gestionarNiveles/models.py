from django.db import models

# Create your models here.
from gestionarEspecialidad.models import Especialidad
from gestionarResultados.models import PlanResultados


class Nivel(models.Model):
    ESTADOS = [
        ('0', 'Eliminado'),
        ('1', 'Activo'),
        ('2', 'Inactivo'),
    ]
    nombre = models.CharField(max_length=100, default='', null=True, blank=True)
    valor = models.IntegerField()
    estado = models.CharField(max_length=2, choices=ESTADOS, default='1', null=True, blank=True)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.DO_NOTHING, null=True)
    plaResultado = models.ForeignKey(PlanResultados, on_delete=models.DO_NOTHING, null=True)

