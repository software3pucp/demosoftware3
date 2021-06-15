from django.db import models

# Create your models here.
from authentication.models import User
from gestionarEspecialidad.models import Especialidad


class PlanMejora(models.Model):
    ESTADOS = [
        ('0', 'Eliminado'),
        ('1', 'Activo'),
        ('2', 'Inactivo'),
    ]
    especialidad = models.ForeignKey(Especialidad, on_delete=models.DO_NOTHING, null=True)
    estado = models.CharField(max_length=2, choices=ESTADOS, default='1', null=True, blank=True)


class PropuestaMejora(models.Model):
    ESTADOS = [
        ('0', 'Eliminado'),
        ('1', 'Activo'),
        ('2', 'Inactivo'),
    ]
    codigo = models.CharField(max_length=10, default='', null=True, blank=True)
    planMejora = models.ForeignKey(PlanMejora, on_delete=models.DO_NOTHING, null=True)
    descripcion = models.CharField(max_length=300, default='', null=True, blank=True)
    estado = models.CharField(max_length=2, choices=ESTADOS, default='1', null=True, blank=True)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.DO_NOTHING, null=True)


class EstadoActividad(models.Model):
    nombre = models.CharField(max_length=300, default='', null=True, blank=True)
    estado = models.IntegerField(default=0)


class ActividadMejora(models.Model):
    codigo = models.CharField(max_length=10, default='', null=True, blank=True)
    descripcion = models.CharField(max_length=300, default='', null=True, blank=True)
    propuestaMejora = models.ForeignKey(PropuestaMejora, on_delete=models.DO_NOTHING)
    estado = models.ForeignKey(EstadoActividad, on_delete=models.DO_NOTHING)
    inicio = models.IntegerField(null=False)
    fin = models.IntegerField(null=False)


class ResponsableMejora(models.Model):
    responsable = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    actividad = models.ForeignKey(ActividadMejora, on_delete=models.DO_NOTHING)
    rol = models.CharField(max_length=100, default='', null=True, blank=True)


class EvidenciaActividadMejora(models.Model):
    ESTADOS = [
        ('0', 'Eliminado'),
        ('1', 'Activo'),
        ('2', 'Inactivo'),
    ]
    estado = models.CharField(max_length=2, choices=ESTADOS, default='1', null=True, blank=True)
    descripcion = models.CharField(max_length=300, default='', null=True, blank=True)
    concepto = models.CharField(max_length=10, default='', null=True, blank=True)
    actividad = models.ForeignKey(ActividadMejora, on_delete=models.DO_NOTHING, null=False)
    archivo = models.FileField(null=True, blank=True, upload_to='mejora/')
    fecha_creacion = models.DateTimeField(auto_now_add=True)