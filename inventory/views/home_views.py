from django.shortcuts import render
from inventory.models import Produto, Estoque, Movimentacao

def home(request):
    total_produtos = Produto.objects.count()
    estoque_baixo = Estoque.objects.filter(quantidade__lte=5).count()
    ultimas_mov = Movimentacao.objects.order_by('-data')[:5]

    return render(request, 'base/base.html', {
        'total_produtos': total_produtos,
        'estoque_baixo': estoque_baixo,
        'ultimas_mov': ultimas_mov
    })