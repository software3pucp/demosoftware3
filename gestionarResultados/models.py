from django.db import models

# Create your models here.

class ResultadoPUCP(models.Model):
    ESTADOS = [
        ('0', 'Eliminado'),
        ('1', 'Activo'),
        ('2', 'Inactivo'),
    ]
    codigo = models.CharField(max_length=10, default='', null=True, blank=True)
    descripcion = models.CharField(max_length=300, default='', null=True, blank=True)
    estado = models.CharField(max_length=2, choices=ESTADOS, default='2', null=True, blank=True)
