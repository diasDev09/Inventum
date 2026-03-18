from django.db import models
from .produto import Produto

class Estoque(models.Model):
    produto = models.OneToOneField(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=0)

    def adicionar(self, quantidade):
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser maior que zero")
        
        self.quantidade += quantidade
        self.save()

    def remover(self, quantidade):
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser maior que zero")

        if quantidade > self.quantidade:
            raise ValueError("Estoque insuficiente")

        self.quantidade -= quantidade
        self.save()

    def __str__(self):
        return f"{self.produto.nome} - {self.quantidade}"