from django.shortcuts import render, redirect, get_object_or_404
from Atividade_1.models import Funcionario
from django.forms import ModelForm

class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'

def lista(request):
    return render(request, 'funcionarios/lista.html', {
        'funcionarios': Funcionario.objects.all()
    })

def insert(request):
    frm = FuncionarioForm(request.POST or None)

    if frm.is_valid():
        frm.save()
        return redirect('funcionarios.lista')

    return render(request, 'funcionarios/form.html', {
        'frm': frm,
        'titulo': 'Cadastrar Funcionário'
    })

def update(request, id):
    funcionario = get_object_or_404(Funcionario, pk=id)
    frm = FuncionarioForm(request.POST or None, instance=funcionario)

    if frm.is_valid():
        frm.save()
        return redirect('funcionarios.lista')

    return render(request, 'funcionarios/form.html', {
        'frm': frm,
        'titulo': 'Atualizar Funcionário'
    })

def delete(request, id):
    funcionario = get_object_or_404(Funcionario, pk=id)
    funcionario.delete()
    return redirect('funcionarios.lista')