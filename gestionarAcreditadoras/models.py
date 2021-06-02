from django.db import models

# Create your models here.

class Acreditadora(models.Model):
    ESTADOS = [
        ('0','Eliminado'),
        ('1','Activo'),
    ]
    nombre = models.CharField(max_length=100,default=None,null=True,blank=True)
    estado = models.CharField(max_length=2,choices=ESTADOS,default=None,null=True,blank=True)