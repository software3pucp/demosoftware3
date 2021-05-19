from django.db import models
from gestionarFacultad.models import Facultad
from gestionarEspecialidad.models import Especialidad
from gestionarCurso.models import Curso
import unicodedata


def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])


# Create your models here.
def substring_after(s, delim):
    return s.rpartition(delim)[-1]


def upload_location(instance, filename):
    extension = substring_after(filename, '.')
    return 'img/%s.%s' % (remove_accents(instance.codigo), extension)


class Horario(models.Model):
    codigo = models.CharField(max_length=30)
    responsable = models.CharField(max_length=50)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True)
