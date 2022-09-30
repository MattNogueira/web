from django.db import models

class Pessoa (models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14)

    def __str__(self):
        return self.cpf

class Habilitacao (models.Model):
    validadeHab = models.CharField(max_length=7)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.SET_NULL, null=True)