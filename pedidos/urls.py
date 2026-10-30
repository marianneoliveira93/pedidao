from django.urls import path
from . import views

urlpatterns = [
    path('cardapio/', views.cardapio, name='cardapio'),
    path('clientes/', views.lista_clientes, name='clientes'),  
    path('pedidos/', views.lista_pedidos, name='pedidos'),
    path('produtos/novo/', views.novo_produto, name='novo_produto'),
    path('pedidos/novo/', views.novo_pedido, name='novo_pedido'),
]