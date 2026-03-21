from inventory.models import Movimentacao
from inventory.services.estoque_service import (
    adicionar_estoque,
    remover_estoque
)


def registrar_entrada(produto, quantidade):
    adicionar_estoque(produto, quantidade)

    mov = Movimentacao(
        produto=produto,
        quantidade=quantidade,
        tipo='E'
    )
    mov.save()

    return mov


def registrar_saida(produto, quantidade):
    remover_estoque(produto, quantidade)

    mov = Movimentacao(
        produto=produto,
        quantidade=quantidade,
        tipo='S'
    )
    mov.save()

    return mov


def listar_movimentacoes():
    return Movimentacao.objects.select_related('produto').order_by('-data')