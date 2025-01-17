from django.db import models

class Plano(models.Model):

    nome = models.CharField(max_length=100)
    preço = models.CharField(max_length=100)
    modalidade = models.CharField(max_length=100)
    dividido = models.BooleanField(default=False)
    cancel_enable = models.BooleanField(default=False)
    aval_gratis = models.BooleanField(default=False)
    roupa = models.BooleanField(default=False)
    garrafinha = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
