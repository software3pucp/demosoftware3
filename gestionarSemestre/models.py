from django.db import models

# Create your models here.

class Semestre(models.Model):
    nombreCodigo = models.CharField(max_length=10)
    anho = models.IntegerField()
    etapa = models.IntegerField()
    inicio = models.DateTimeField(null =True, blank= True)
    fin = models.DateTimeField(null =True, blank= True)