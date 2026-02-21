from django.db import models

class Confirmacao(models.Model):
    nome_responsavel = models.CharField(max_length=100)
    email = models.EmailField()
    quantidade_criancas = models.PositiveIntegerField()
    confirmado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_responsavel