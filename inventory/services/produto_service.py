from inventory.repositories.produto_repository import (
    listar_produtos,
    buscar_produto_por_id,
    criar_produto,
    atualizar_produto,
    deletar_produto
)


def listar_produtos_service():
    return listar_produtos()


def criar_produto_service(form):
    if not form.is_valid():
        raise ValueError("Dados inválidos")

    return criar_produto(form.cleaned_data)


def atualizar_produto_service(produto_id, form):
    if not form.is_valid():
        raise ValueError("Dados inválidos")

    produto = buscar_produto_por_id(produto_id)

    return atualizar_produto(produto, form.cleaned_data)


def deletar_produto_service(produto_id):
    produto = buscar_produto_por_id(produto_id)
    deletar_produto(produto)