from django.db import models
from gestionarEspecialidad.models import Especialidad
import unicodedata


def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])


# Create your models here.
def substring_after(s, delim):
    return s.rpartition(delim)[-1]


def upload_location(instance, filename):
    extension = substring_after(filename, '.')
    return 'evidencias/horarios/%s.%s' % (remove_accents(instance.nombre), extension)


class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, null=True)
    ESTADOS = [
        ('0', 'Eliminado'),
        ('1', 'Activo'),
        ('2', 'Inactivo'),
    ]
    estado = models.CharField(max_length=2, choices=ESTADOS, default=None, null=True, blank=True)

