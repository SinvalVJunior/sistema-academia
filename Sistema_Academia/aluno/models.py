from django.db import models
from secretario.models import *
from django import template
from professor.models import Treino
from medico.models import Exame

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
    password = models.CharField(max_length=100)
    planos = models.ManyToManyField(Plano,default=None)

    treino = models.ManyToManyField(Treino,default=None)

    exame = models.ManyToManyField(Exame,default=None)
    
    def __str__(self):
        return self.nome

class Modalidade(models.Model):
    name = models.CharField(max_length=100)
    max_alunos = models.IntegerField()
    def __str__(self):
        return self.name
class Aula(models.Model):
    
    name = models.CharField(max_length=100)
    modalidade = models.ManyToManyField(Modalidade)
    dia = models.CharField(max_length=100,default="")
    horario = models.CharField(max_length=100)
    alunos = models.ManyToManyField(Aluno)

    def __str__(self):
        return self.name





