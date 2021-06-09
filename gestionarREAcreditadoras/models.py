from django.db import models

# Create your models here.
from gestionarAcreditadoras.models import Acreditadora
from gestionarIndicadores.models import Indicador
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

