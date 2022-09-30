from django.db import models

class Departamento (models.Model):
    desc = models.CharField(max_length=500)

    def __str__(self):
        return self.desc

class Funcionario (models.Model):
    nome = models.CharField(max_length=500)
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True)