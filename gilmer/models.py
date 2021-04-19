from django.db import models

class Pubgmteams(models.Model):
    name = models.CharField(max_length=100)
    numPlayers = models.IntegerField(default=0)
    region = models.CharField(max_length=100)
    igl = models.CharField(max_length=100, null=True, blank=True)
    scout = models.CharField(max_length=100, null=True, blank=True)
    carry = models.CharField(max_length=100, null=True, blank=True)
    support = models.CharField(max_length=100, null=True, blank=True)
    sniper = models.CharField(max_length=100, null=True, blank=True)
    estado = models.IntegerField(default=1)
