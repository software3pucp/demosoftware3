from django.db import models

# Create your models here.

class Especialidad(models.Model):
    nombre = models.CharField(max_length=30)
    responsable = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='img/')
    inicio = models.CharField(max_length=20, null=True)
    fin = models.CharField(max_length=20, null=True)
