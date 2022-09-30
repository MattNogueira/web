from django.shortcuts import render, redirect, get_object_or_404
from Atividade_3.models import Telefone
from django.forms import ModelForm

class TelefoneForm(ModelForm):
    class Meta:
        model = Telefone
        fields = '__all__'

def lista(request):
    return render(request, 'telefones/lista.html', {
        'telefones': Telefone.objects.all()
    })

def insert(request):
    frm = TelefoneForm(request.POST or None)

    if frm.is_valid():
        frm.save()
        return redirect('telefones.lista')

    return render(request, 'telefones/form.html', {
        'frm': frm,
        'titulo': 'Cadastrar Telefone'
    })

def update(request, id):
    telefone = get_object_or_404(Telefone, pk=id)
    frm = TelefoneForm(request.POST or None, instance=telefone)

    if frm.is_valid():
        frm.save()
        return redirect('telefones.lista')

    return render(request, 'telefones/form.html', {
        'frm': frm,
        'titulo': 'Atualizar Telefone'
    })

def delete(request, id):
    telefone = get_object_or_404(Telefone, pk=id)
    telefone.delete()
    return redirect('telefones.lista')