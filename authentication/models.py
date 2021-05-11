from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    estado = models.BooleanField(default=False)
    codigo = models.CharField(max_length=15)
    genero = models.CharField(max_length=2)
    foto = models.ImageField(upload_to='usuarios/', null=True)
