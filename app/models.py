from django.db import models


# Criando novos modelos
class Carros(models.Model):
    Nome_Completo = models.CharField(max_length=150)
    Senha = models.CharField(max_length=100)
    Confirme_sua_Senha = models.CharField(max_length=100)
    CEP = models.IntegerField()
    Estado = models.CharField(max_length=100)
    Rua = models.CharField(max_length=100)
    Numero = models.IntegerField()
    Ponto_de_Referencia = models.CharField(max_length=100)