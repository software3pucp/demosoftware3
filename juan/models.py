# Create your models here.

from django.db import models


class Characters(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    weapon = models.CharField(max_length=100)
    image = models.CharField(max_length=300 , null=True)



