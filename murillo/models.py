from django.db import models

class Tipo(models.Model):
    nombre=models.CharField(max_length=100)
    color = models.CharField(max_length=7,null=True)

class Pokemon(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.ForeignKey(Tipo,on_delete=models.CASCADE)
    altura = models.FloatField()
    peso = models.FloatField()
    estado = models.IntegerField(default=1)
    imagen = models.CharField(max_length=140,null=True)