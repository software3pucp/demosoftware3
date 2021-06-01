from django.db import models

# Create your models here.

class Semestre(models.Model):
    nombreCodigo = models.CharField(max_length=10, unique=True,blank=True, null=True)
    anho = models.IntegerField(null=True)
    etapa = models.IntegerField(null=True)
    inicio = models.CharField(max_length=20, null=True)
    fin = models.CharField(max_length=20, null=True)