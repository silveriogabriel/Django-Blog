from django.db import models
from django.contrib.auth.models import User

class simulacoes(models.Model):
    banca_inicial = models.FloatField()
    stopgain = models.FloatField()
    stoploss = models.FloatField()
    banca_atual = models.FloatField()
    green = models.FloatField()
    red = models.FloatField()
    primeira_entrada = models.FloatField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True)
    created = models.TimeField(auto_now_add=True)
    jogada = models.CharField(max_length=255)