from django.db import models
from secretario.models import *

class Aluno(models.Model):
    
    nome = models.CharField(max_length=100)
    CPF = models.CharField(max_length=100)
    identidade = models.CharField(max_length=100)
    nascimento = models.CharField(max_length=20)

    n_cartao = models.CharField(max_length=100)
    bandeira = models.CharField(max_length=100)
    cartao_nome = models.CharField(max_length=100)

    usuario = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    planos = models.ManyToManyField(Plano,default=None)

    def __str__(self):
        return self.nome



class Aula(models.Model):
    
    name = models.CharField(max_length=100)
    modalidade = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    max_alunos = models.IntegerField()
    alunos = models.ManyToManyField(Aluno)

    def __str__(self):
        return self.name


class Dia(models.Model):
    dia = models.CharField(max_length=100)
    aulas = models.ManyToManyField(Aula)

    def __str__(self):
        return self.dia