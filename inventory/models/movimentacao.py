from django.db import models
from .produto import Produto
from .estoque import Estoque

class Movimentacao(models.Model):

    TIPO_CHOICES = [
        ('E', 'Entrada'),
        ('S', 'Saída'),
    ]

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    quantidade = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        estoque, _ = Estoque.objects.get_or_create(produto=self.produto)

        if self.tipo == 'E':
            estoque.quantidade += self.quantidade
        elif self.tipo == 'S':
            estoque.quantidade -= self.quantidade

        estoque.save()

        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.produto.nome} - {self.get_tipo_display()} - {self.quantidade}"