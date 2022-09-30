"""Atividade_1 URL Configuration

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
from django.contrib import admin
from django.urls import path
from Atividade_1.views import pages, funcionario, departamento

urlpatterns = [
    path('', pages.home, name='home'),
    path('funcionarios', funcionario.lista, name='funcionarios.lista'),
    path('funcionarios/inserir', funcionario.insert, name='funcionarios.insert'),
    path('funcionarios/atualizar/<id>', funcionario.update, name='funcionarios.update'),
    path('funcionarios/deletar/<id>', funcionario.delete, name='funcionarios.delete'),
    path('departamentos', departamento.lista, name="departamentos.lista"),
    path('departamentos/inserir', departamento.insert, name='departamentos.insert'),
    path('departamentos/atualizar/<id>', departamento.update, name='departamentos.update'),
    path('departamentos/deletar/<id>', departamento.delete, name='departamentos.delete')
]
