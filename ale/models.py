from django.db import models

# Create your models here.

from django.db import models


class Personaje(models.Model):
    name = models.CharField(max_length=100)
    edad = models.IntegerField(default=0)
    sexo = models.CharField(max_length=1)