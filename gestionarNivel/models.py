from django.db import models

# Create your models here.
class Nivel(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField()
    state = models.IntegerField(default=1)
