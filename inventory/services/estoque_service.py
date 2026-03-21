from inventory.repositories.estoque_repository import (
    obter_estoque_por_produto,
    salvar_estoque
)

def adicionar_estoque(produto, quantidade):
    estoque = obter_estoque_por_produto(produto)
    estoque.quantidade += quantidade
    return salvar_estoque(estoque)


def remover_estoque(produto, quantidade):
    estoque = obter_estoque_por_produto(produto)

    if quantidade > estoque.quantidade:
        raise ValueError("Estoque insuficiente")

    estoque.quantidade -= quantidade
    return salvar_estoque(estoque)