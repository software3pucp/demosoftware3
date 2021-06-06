from django.db import models

# Create your models here.
from gestionarHorario.models import Horario
import unicodedata


def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

# Create your models here.
def substring_after(s, delim):
    return s.rpartition(delim)[-1]

def upload_location_archive(instance, filename):
    extension = substring_after(filename, '.')
    return 'archive/%s.%s' % (remove_accents(instance.horario.codigo), extension)

class EvidenciasxHorario(models.Model):
    ESTADOS = [
        ('0', 'Eliminado'),
        ('1', 'Activo'),
        ('2', 'Inactivo'),
    ]
    estado = models.CharField(max_length=2, choices=ESTADOS, default='1', null=True, blank=True)
    horario = models.ForeignKey(Horario, on_delete=models.DO_NOTHING, null=False)
    archivo = models.FileField(null=True, blank=True, upload_to='archive/')