
from django.db import models
from django.contrib.auth.models import User

# python manage.py makemigrations -> Compila en cajanegra el model -> Sql
# python manage.py migrate -> Ejecuta el codigo en sql (precompilado) y crea las tablas


# Create your models here.
#AQUI VAN LAS BBDD

# LENGUAJE
# id (autogenerado, consecutivo)
# nombre -> string(50)
# longitud del nombre -> int
# do_i_speak_it -> Bool

class Language(models.Model):
    name = models.CharField(max_length=200)
    lenName = models.IntegerField(default=0, null=True, blank=True)
    doISpeakIt = models.BooleanField(default=False)








