
from django.db import models
from django.conf import settings

from authentication.models import User
from gestionarFacultad.models import Facultad
import unicodedata


def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])


# Create your models here.
def substring_after(s, delim):
    return s.rpartition(delim)[-1]


def upload_location(instance, filename):
    extension = substring_after(filename, '.')
    return 'img/%s.%s' % (remove_accents(instance.nombre), extension)


class Especialidad(models.Model):
    nombre = models.CharField(max_length=30)
    responsable = models.CharField(max_length=50)
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE, null=True)
    foto = models.ImageField(null=True, blank=True, upload_to=upload_location)
    ESTADOS = [
        ('0', 'Eliminado'),
        ('1', 'Activo'),
        ('2', 'Inactivo'),
    ]
    estado = models.CharField(max_length=2, choices=ESTADOS, default=None, null=True, blank=True)
    codigo = models.CharField(max_length=4,null=True,blank=True,default='')
    versiones = models.IntegerField(max_length=10000,default=0,null=True,blank=True)

class Asistente(models.Model):
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Auditor(models.Model):
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)