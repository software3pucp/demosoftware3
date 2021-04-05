from django.db import models


class Champion(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    tipo = models.CharField(max_length=100)
    foto = models.CharField(max_length=2000, null=True)
