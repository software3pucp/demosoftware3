from django.db import models

# Create your models here.
from gestionarResultados.models import ResultadoPUCP


class Acreditadora(models.Model):
    ESTADOS = [
        ('0','Eliminado'),
        ('1','Activo'),
    ]
    nombre = models.CharField(max_length=100,default=None,null=True,blank=True)
    estado = models.CharField(max_length=2,choices=ESTADOS,default=None,null=True,blank=True)


class ResultadoAcreditadora(models.Model):
    ESTADOS = [
        ('0','Eliminado'),
        ('1','Activo'),
        ('2','Inactivo'),
    ]
    codigo = models.CharField(max_length=10,default='',null=True,blank=True)
    descripcion = models.CharField(max_length=150,default='',null=True,blank=True)
    estado = models.CharField(max_length=2,choices=ESTADOS,default='2',null=True,blank=True)
    acreditadora = models.ForeignKey(Acreditadora,on_delete=models.RESTRICT)
    resultadoPUCP = models.ForeignKey(ResultadoPUCP,on_delete=models.RESTRICT)
