from django.db import models

# Create your models here.
from gestionarAcreditadoras.models import Acreditadora
from gestionarResultados.models import ResultadoPUCP


class ResultadoAcreditadora(models.Model):
    ESTADOS = [
        ('0','Eliminado'),
        ('1','Activo'),
        ('2','Inactivo'),
    ]
    codigo = models.CharField(max_length=10,default='',null=True,blank=True)
    descripcion = models.CharField(max_length=150,default='',null=True,blank=True)
    estado = models.CharField(max_length=2,choices=ESTADOS,default='1',null=True,blank=True)
    acreditadora = models.ForeignKey(Acreditadora,on_delete=models.RESTRICT, null=True)
    # indicador=models.ForeignKey(Indicador,on_delete=models.DO_NOTHING,null=True)

class REAcred_REPucp(models.Model):
    ESTADOS = [
        ('0', 'Eliminado'),
        ('1', 'Activo'),
        ('2','Inactivo'),
    ]
    resultadoAcreditadora = models.ForeignKey(ResultadoAcreditadora, on_delete=models.DO_NOTHING, null=True)
    resultadoPUCP = models.ForeignKey(ResultadoPUCP, on_delete=models.DO_NOTHING, null=True)
    estado = models.CharField(max_length=2, choices=ESTADOS, default='1', null=True, blank=True)

class HistoriaREAcred(models.Model):
    resultadoAcreditadora = models.ForeignKey(ResultadoAcreditadora, on_delete=models.DO_NOTHING, null=True)
    codIndicador=models.CharField(max_length=10,default='',null=True,blank=True)
    descpIndicador=models.CharField(max_length=150, default='', null=True, blank=True)
    facultad=models.CharField(max_length=150, default='', null=True, blank=True)
    especialidad=models.CharField(max_length=150, default='', null=True, blank=True)
