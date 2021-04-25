# Create your models here.

from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=100)
    longitud = models.IntegerField(default=0)
    foto = models.ImageField(upload_to='Language/img',null=True, blank=True)
    file = models.FileField(upload_to='Language/files',null=True, blank=True)
    habloElIdioma = models.BooleanField(default=False, null=True, blank=True)


class LanguageLearned(models.Model):
    language = models.ForeignKey(Language, on_delete=models.DO_NOTHING, )
    state = models.IntegerField(default=0)






