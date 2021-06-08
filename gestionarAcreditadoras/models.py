from django.db import models
import unicodedata
# Create your models here.

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])


# Create your models here.
def substring_after(s, delim):
    return s.rpartition(delim)[-1]


def upload_location(instance, filename):
    extension = substring_after(filename, '.')
    return 'img/%s.%s' % (remove_accents(instance.nombre), extension)

class Acreditadora(models.Model):
    ESTADOS = [
        ('0','Eliminado'),
        ('1','Activo'),
        ('2','Inactivo'),
    ]
    nombre = models.CharField(max_length=100,default='',null=True,blank=True)
    foto = models.ImageField(null=True, blank=True, upload_to=upload_location)
    estado = models.CharField(max_length=2,choices=ESTADOS,default='1',null=True,blank=True)