from django.db import models

# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=100)
    longitud = models.IntegerField(default=0)
    habloElIdioma = models.BooleanField(default=False, null=True, blank=True)

class Pais(models.Model):
    name = models.CharField(max_length=100)
    capital = models.CharField(max_length=100, null=True, blank=True)

class PaisIdioma(models.Model):
    idPais = models.IntegerField()
    idLanguage = models.IntegerField()