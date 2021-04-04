# Create your models here.

from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=100)
    longitud = models.IntegerField(default=0)
    habloElIdioma = models.BooleanField(default=False, null=True, blank=True)










