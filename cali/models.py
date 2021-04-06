from django.db import models

# Create your models here.
from django.db import models


class Candidato(models.Model):
    nombre = models.CharField(max_length=100)
    nombCandidato = models.CharField(max_length=150)
    postura = models.CharField(max_length=150,null = True,blank = True)
    fecha = models.DateTimeField(null =True, blank= True)
