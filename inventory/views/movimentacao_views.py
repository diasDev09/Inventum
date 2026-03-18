from django.shortcuts import render, redirect
from inventory.models import Movimentacao, Produto
from inventory.forms.movimentacao_form import MovimentacaoForm


def entrada_produto(request):
    if request.method == 'POST':
        form = MovimentacaoForm(request.POST)
        if form.is_valid():
            mov = form.save(commit=False)
            mov.tipo = 'E'
            mov.save()
            return redirect('historico_movimentacoes')
    else:
        form = MovimentacaoForm()

    return render(request, 'movimentacao/entrada.html', {'form': form})


def saida_produto(request):
    if request.method == 'POST':
        form = MovimentacaoForm(request.POST)
        if form.is_valid():
            mov = form.save(commit=False)
            mov.tipo = 'S'
            mov.save()
            return redirect('historico_movimentacoes')
    else:
        form = MovimentacaoForm()

    return render(request, 'movimentacao/saida.html', {'form': form})


def historico_movimentacoes(request):
    movimentacoes = Movimentacao.objects.all().select_related('produto').order_by('-data')

    return render(request, 'movimentacao/historico.html', {
        'movimentacoes': movimentacoes
    })