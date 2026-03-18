from django.shortcuts import render, get_object_or_404, redirect
from inventory.models import Produto
from inventory.forms.produto_form import ProdutoForm


# Lista de produtos 
def lista_produtos(request):
    produtos = Produto.objects.all().select_related('categoria')

    return render(request, 'produto/list.html', {
        'produtos': produtos
    })

# função para Upar os produtos  
def update_produto(request, id):
    produto = get_object_or_404(Produto, id=id)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'produto/update.html', {
        'form': form
    })

# Função criar produto
def create_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()

    return render(request, 'produto/create.html', {
        'form': form
    })
    
# Funçâo Delete
def delete_produto(request, id):
    produto = get_object_or_404(Produto, id=id)

    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')

    return render(request, 'produto/delete.html', {
        'produto': produto
    })