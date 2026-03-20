from django.shortcuts import render, get_object_or_404, redirect
# import models
from inventory.models import Produto
from inventory.forms.produto_form import ProdutoForm
# import services
from inventory.services.produto_service import listar_produtos_service
from inventory.services.produto_service import criar_produto_service
from inventory.services.produto_service import atualizar_produto_service
from inventory.services.produto_service import deletar_produto_service

# Lista de Produtos 
def lista_produtos(request):
    produtos = listar_produtos_service()
    
    return render(request, 'produto/list.html', {
        'produtos':produtos
    })

# Criar Produtos 
def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)

        try:
            criar_produto_service(form)
            return redirect('lista_produtos')
        except ValueError:
            pass
    else:
        form = ProdutoForm()

    return render(request, 'produto/create.html', {'form': form})

# Atualizar Produtos 
def atualizar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)

        try:
            atualizar_produto_service(id, form)
            return redirect('lista_produtos')
        except ValueError:
            pass
    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'produto/update.html', {'form': form})

# Deletar Produtos 
def deletar_produto(request, id):
    deletar_produto_service(id)
    return redirect('lista_produtos')