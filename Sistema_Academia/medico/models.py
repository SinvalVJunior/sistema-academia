from django.db import models
from academia.models import Academia_Users


class Exame(models.Model):

    cpf_aluno = models.CharField(max_length=100)
    peso = models.CharField(max_length=100)
    altura = models.CharField(max_length=100)
    pressao = models.CharField(max_length=100)
    pgc = models.CharField(max_length=100)
    pmm = models.CharField(max_length=100)
    imc = models.CharField(max_length=100)
    habilitado = models.CharField(max_length=4)
    id_medico = models.CharField(max_length=100)

    def __str__(self):
        return  self.id_medico + " - " + self.cpf_aluno