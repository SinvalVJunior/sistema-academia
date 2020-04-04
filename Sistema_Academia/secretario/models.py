from django.db import models

class Plano(models.Model):

    name = models.CharField(max_length=100)
    preço = models.CharField(max_length=100)
    musculação = models.BooleanField(default=False)
    crossfit = models.BooleanField(default=False)
    spinning = models.BooleanField(default=False)
    natação = models.BooleanField(default=False)
    ritmos = models.BooleanField(default=False)
    dividido = models.BooleanField(default=False)
    cancel_enable = models.BooleanField(default=False)
    aval_gratis = models.BooleanField(default=False)

    def __str__(self):
        return self.name
