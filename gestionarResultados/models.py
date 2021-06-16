from django.db import models

# Create your models here.
from gestionarEspecialidad.models import Especialidad
from gestionarSemestre.models import Semestre


class ResultadoPUCP(models.Model):
    ESTADOS = [
        ('0', 'Eliminado'),
        ('1', 'Activo'),
        ('2', 'Inactivo'),
    ]
    codigo = models.CharField(max_length=10, default='', null=True, blank=True)
    descripcion = models.CharField(max_length=300, default='', null=True, blank=True)
    estado = models.CharField(max_length=2, choices=ESTADOS, default='1', null=True, blank=True)
    especialidad = models.ForeignKey(Especialidad,on_delete=models.DO_NOTHING, null=True)

class PlanResultados(models.Model):
    ESTADOS = [
        ('0', 'Eliminado'),
        ('1', 'Activo'),
        ('2', 'Inactivo'),
    ]
    codigo = models.CharField(max_length=10, default='', null=True, blank=True)
    descripcion = models.CharField(max_length=300, default='', null=True, blank=True)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.RESTRICT)
    semestre = models.ForeignKey(Semestre, on_delete=models.RESTRICT)
    estado = models.CharField(max_length=2, choices=ESTADOS, default='1', null=True, blank=True)
    resultados = models.ManyToManyField(ResultadoPUCP)
