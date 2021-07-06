from django.db import models
# Create your models here.
from gestionarResultados.models import ResultadoPUCP
from gestionarREAcreditadoras.models import ResultadoAcreditadora


class Indicador(models.Model):
    codigo = models.CharField(max_length=10, default='', null=True, blank=True)
    descripcion = models.CharField(max_length=150, default='', null=True, blank=True)
    resultado = models.ForeignKey(ResultadoPUCP, on_delete=models.CASCADE, null=True)
    resultadoAcreditadora = models.ForeignKey(ResultadoAcreditadora, on_delete=models.CASCADE, null=True)
    estado = models.IntegerField(default=1)