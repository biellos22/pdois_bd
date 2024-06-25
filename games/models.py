# games/models.py
from django.db import models

class Game(models.Model):
    nome = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    data_de_lancamento = models.DateField()

    def __str__(self):
        return self.nome
