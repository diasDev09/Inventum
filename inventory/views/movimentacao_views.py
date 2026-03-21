from django.shortcuts import render, redirect
from django.contrib import messages
from inventory.forms.movimentacao_form import MovimentacaoForm
from inventory.services.movimentacao_service import (
    registrar_entrada,
    registrar_saida,
    listar_movimentacoes
)


def entrada_produto(request):
    if request.method == 'POST':
        form = MovimentacaoForm(request.POST)
        if form.is_valid():
            produto = form.cleaned_data['produto']
            quantidade = form.cleaned_data['quantidade']

            registrar_entrada(produto, quantidade)

            messages.success(request, "Entrada registrada com sucesso!")
            return redirect('historico_movimentacoes')
    else:
        form = MovimentacaoForm()

    return render(request, 'movimentacao/entrada.html', {'form': form})


def saida_produto(request):
    if request.method == 'POST':
        form = MovimentacaoForm(request.POST)
        if form.is_valid():
            produto = form.cleaned_data['produto']
            quantidade = form.cleaned_data['quantidade']

            try:
                registrar_saida(produto, quantidade)
                messages.success(request, "Saída registrada com sucesso!")
                return redirect('historico_movimentacoes')

            except ValueError as e:
                messages.error(request, str(e))
                return redirect('saida_produto')
    else:
        form = MovimentacaoForm()

    return render(request, 'movimentacao/saida.html', {'form': form})


def historico_movimentacoes(request):
    movimentacoes = listar_movimentacoes()

    return render(request, 'movimentacao/historico.html', {
        'movimentacoes': movimentacoes
    })