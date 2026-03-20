from django.shortcuts import render
from inventory.models import Produto, Estoque, Movimentacao

def dashboard(request):
    context = {
        'total_produtos': Produto.objects.count(),
        'estoque_baixo': Estoque.objects.filter(quantidade__lte=5).count(),
        'movimentacoes': Movimentacao.objects.order_by('-data')[:5]
    }

    return render(request, 'estoque/dashboard.html', context)