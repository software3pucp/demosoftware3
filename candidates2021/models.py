from django.db import models

class Candidate(models.Model):
    name=models.CharField(max_length=100)
    partido=models.CharField(max_length=100)
    sex=models.BooleanField
    edad=models.IntegerField
    foto=models.ImageField(null=True)