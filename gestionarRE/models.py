from django.db import models

# Create your models here.


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
    ]
    codigo = models.CharField(max_length=10,default='',null=True,blank=True)
    descripcion = models.CharField(max_length=150,default='',null=True,blank=True)
    estado = models.CharField(max_length=2,choices=ESTADOS,default='1',null=True,blank=True)
    acreditadora = models.ForeignKey(Acreditadora,on_delete=models.RESTRICT)


class Resultado(models.Model):
    codigo = models.CharField(max_length=10,default=None,null=True,blank=True)
    descripcion = models.CharField(max_length=150,default=None,null=True,blank=True)
    resultadosAcreditadora = models.ManyToManyField(ResultadoAcreditadora)
