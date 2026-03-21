from inventory.models import Estoque

def obter_estoque_por_produto(produto):
    estoque, _ = Estoque.objects.get_or_create(produto=produto)
    return estoque

def salvar_estoque(estoque):
    estoque.save()
    return estoque