from django.db import models
from .produto import Produto


class Estoque(models.Model):
    produto = models.OneToOneField(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.produto.nome} - {self.quantidade}"