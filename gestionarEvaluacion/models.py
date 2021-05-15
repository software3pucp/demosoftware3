from django.db import models

# Create your models here.

class Alumno(models.Model):
    nombreAlumno = models.CharField(max_length=10,null=True,blank=True)
    codigoAlumno = models.CharField(max_length=9,null=True,blank=True)