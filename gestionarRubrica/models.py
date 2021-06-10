from django.db import models

# Create your models here.
from gestionarEspecialidad.models import Especialidad
from gestionarIndicadores.models import Indicador
from gestionarNiveles.models import Nivel


class Rubrica(models.Model):
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, null=True)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE, null=True)
    indicador = models.ForeignKey(Indicador, on_delete=models.CASCADE, null=True)
    descripcion = models.CharField(max_length=200, default='', null=True, blank=True)