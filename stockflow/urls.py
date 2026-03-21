"""
URL configuration for stockflow project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from inventory.views.dashboard_views import dashboard
from inventory.views.produto_views import (
    lista_produtos,
    criar_produto,
    atualizar_produto,
    deletar_produto
)
from inventory.views.movimentacao_views import entrada_produto, saida_produto, historico_movimentacoes


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='home'),
    path('', TemplateView.as_view(template_name="base/base.html"), name='home'),
    path('produtos/', lista_produtos, name='lista_produtos'),
    path('/produtos/criar/', criar_produto, name='criar_produto'),
    path('produtos/editar/<int:id>/', atualizar_produto, name='atualizar_produto'),
    path('produtos/deletar/<int:id>/', deletar_produto, name='deletar_produto'),
    path('movimentacoes/entrada/', entrada_produto, name='entrada_produto'),
    path('movimentacoes/saida/', saida_produto, name='saida_produto'),
    path('movimentacoes/', historico_movimentacoes, name='historico_movimentacoes'),
]
