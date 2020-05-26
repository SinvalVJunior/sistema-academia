from django.db import models
from academia.models import Academia_Users


class Treino(models.Model):

    nome = models.CharField(max_length=100)
    peito = models.CharField(max_length=100)
    ombro = models.CharField(max_length=100)
    biceps = models.CharField(max_length=100)
    costas = models.CharField(max_length=100)
    triceps = models.CharField(max_length=100)
    professor = models.ManyToManyField(Academia_Users,default=None)

    def __str__(self):
        return self.nome