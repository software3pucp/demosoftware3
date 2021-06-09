from django.db import models

# Create your models here.

class Historico(models.Model):
    nombreHistorico = models.CharField(max_length=10, unique=True,blank=True, null=True)