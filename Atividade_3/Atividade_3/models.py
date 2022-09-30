from django.db import models

class Corretor(models.Model):
    cpf = models.CharField(max_length=14, unique=True)
    nome = models.CharField(max_length=60)
    comissao = models.IntegerField()

    def __str__(self):
        return self.nome

class Telefone(models.Model):
    area = models.CharField(max_length=2)
    numero = models.CharField(max_length=9)
    corretor = models.ForeignKey(Corretor, on_delete=models.CASCADE, null=True)

class CGerenciaC(models.Model):
    cpfCorretor = models.ForeignKey(Corretor, on_delete=models.SET_NULL, null=True, related_name='Gerenciado')
    cpfGerente = models.ForeignKey(Corretor, on_delete=models.SET_NULL, null=True, related_name='Gerente')

class Regiao(models.Model):
    nome = models.CharField(max_length=60)
    corretores = models.ManyToManyField(Corretor)

    def __str__(self):
        return self.nome

class Municipio(models.Model):
    uf = models.CharField(max_length=2)
    nome = models.CharField(max_length=300)
    regiao = models.ForeignKey(Regiao, on_delete=models.CASCADE, null=True) 

class CorretorARegiao(models.Model):
    regiao = models.ForeignKey(Regiao, on_delete=models.CASCADE, null=True)
    corretor = models.ForeignKey(Corretor, on_delete=models.CASCADE, null=True)