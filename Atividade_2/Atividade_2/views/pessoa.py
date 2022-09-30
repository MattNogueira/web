from django.shortcuts import render, get_object_or_404, redirect
from Atividade_2.models import Pessoa
from django.forms import ModelForm

class PessoaForm (ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'

def lista(request):
    return render(request, 'pessoas/lista.html', {
        'pessoas': Pessoa.objects.all()
    })

def insert(request):
    frm = PessoaForm(request.POST or None)

    if frm.is_valid():
        frm.save()
        return redirect('pessoas.lista')

    return render(request, 'pessoas/form.html', {
        'frm':frm,
        'titulo':'Cadastrar Pessoa'
    })

def update(request, id):
    pessoa = get_object_or_404(Pessoa, pk=id)
    frm = PessoaForm(request.POST or None, instance=pessoa)

    if frm.is_valid():
        frm.save()
        return redirect('pessoas.lista')

    return render(request, 'pessoas/form.html', {
        'frm':frm,
        'titulo':'Atualizar Pessoa'
    })

def delete(request, id):
    pessoa = get_object_or_404(Pessoa, pk=id)
    pessoa.delete()
    return redirect('pessoas.lista')