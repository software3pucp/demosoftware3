from django.db import models

# Create your models here.

class Especialidad(models.Model):
    nombre = models.CharField(max_length=30)
    responsable = models.CharField(max_length=50)
    foto = models.ImageField(null=True, blank=True, upload_to='img/')