from inventory.models import Produto


def listar_produtos():
    return Produto.objects.select_related('categoria').all()


def buscar_produto_por_id(produto_id):
    return Produto.objects.get(id=produto_id)


def criar_produto(data):
    return Produto.objects.create(**data)


def atualizar_produto(produto, data):
    for campo, valor in data.items():
        setattr(produto, campo, valor)
    produto.save()
    return produto


def deletar_produto(produto):
    produto.delete()