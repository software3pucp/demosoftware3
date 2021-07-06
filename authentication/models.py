from django.db import models
from django.contrib.auth.models import AbstractUser
import unicodedata
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from gestionarFacultad.models import Facultad
from gestionarEspecialidad.models import Especialidad
# Create your models here.
def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])


# Create your models here.
def substring_after(s, delim):
    return s.rpartition(delim)[-1]


def upload_location(instance, filename):
    extension = substring_after(filename, '.')
    return 'img/%s.%s' % (remove_accents(instance.first_name), extension)


class User(AbstractUser):
    ESTADOS = [
        ('0', 'Eliminado'),
        ('1', 'Activo'),
        ('2', 'Inactivo'),
    ]
    estado = models.CharField(max_length=2, choices=ESTADOS, default='1', null=True, blank=True)
    code = models.CharField(max_length=8, default='11111111')
    photo = models.ImageField(null=True, blank=True, upload_to=upload_location)
    rol_actual = models.CharField(max_length=50, default=None, null=True, blank=True)
    n_Roles = models.CharField(max_length=2, default=None, null=True, blank=True)
    token = models.UUIDField(primary_key=False, editable=False, null=True, blank=True)


class UserxGroups(models.Model):
    user = models.ForeignKey(User,on_delete= models.DO_NOTHING)
    group = models.ForeignKey(Group,on_delete= models.DO_NOTHING)
    facultad = models.ForeignKey(Facultad,on_delete= models.DO_NOTHING,null=True)
    especialidad = models.ForeignKey(Especialidad,on_delete= models.DO_NOTHING,null=True)



