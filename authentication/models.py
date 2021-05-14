from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    code = models.CharField(max_length=8,default='11111111')
    photo = models.ImageField(upload_to='usuarios/', null=True)
