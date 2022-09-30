"""Atividade_3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from Atividade_3.views import pages, corretor, regiao, municipio, telefone

urlpatterns = [
    path('', pages.home, name='home'),
    path('corretores', corretor.lista, name='corretores.lista'),
    path('corretores/inserir', corretor.insert, name='corretores.insert'),
    path('corretores/atualizar/<id>', corretor.update, name='corretores.update'),
    path('corretores/deletar/<id>', corretor.delete, name='corretores.delete'),
    path('regioes', regiao.lista, name="regioes.lista"),
    path('regioes/inserir', regiao.insert, name='regioes.insert'),
    path('regioes/atualizar/<id>', regiao.update, name='regioes.update'),
    path('regioes/deletar/<id>', regiao.delete, name='regioes.delete'),
    path('municipios', municipio.lista, name="municipios.lista"),
    path('municipios/inserir', municipio.insert, name='municipios.insert'),
    path('municipios/atualizar/<id>', municipio.update, name='municipios.update'),
    path('municipios/deletar/<id>', municipio.delete, name='municipios.delete'),
    path('telefones', telefone.lista, name="telefones.lista"),
    path('telefones/inserir', telefone.insert, name='telefones.insert'),
    path('telefones/atualizar/<id>', telefone.update, name='telefones.update'),
    path('telefones/deletar/<id>', telefone.delete, name='telefones.delete')
]
