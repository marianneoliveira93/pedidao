from django.shortcuts import render, redirect
from .models import Produto, Cliente, Pedido
from .forms import ProdutoForm, PedidoForm

def cardapio(request):
    produtos = Produto.objects.all()
    return render(
        request,
        'pedidos/cardapio.html',
        {'produtos': produtos},
    )


def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(
        request,
        'pedidos/lista_pedidos.html',
        {'pedidos': pedidos},
    )


def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(
        request,
        'pedidos/lista_clientes.html',
        {'clientes': clientes},
    )


def novo_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cardapio')
    else:
        form = ProdutoForm()

    return render(
        request,
        'pedidos/produto_form.html',
        {'form': form},
    )

def novo_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pedidos')
    else:
        form = PedidoForm()

    return render(
        request,
        'pedidos/pedido_form.html',
        {'form': form},
    )