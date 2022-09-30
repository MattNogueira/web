from django.shortcuts import render, redirect, get_object_or_404
from Atividade_3.models import Regiao
from django.forms import ModelForm

class RegiaoForm(ModelForm):
    class Meta:
        model = Regiao
        fields = '__all__'

def lista(request):
    return render(request, 'regioes/lista.html', {
        'regioes': Regiao.objects.all()
    })

def insert(request):
    frm = RegiaoForm(request.POST or None)

    if frm.is_valid():
        frm.save()
        return redirect('regioes.lista')
    
    return render(request, 'regioes/form.html', {
        'frm': frm,
        'titulo': 'Cadastrar Regiao'
    })

def update(request, id):
    regiao = get_object_or_404(Regiao, pk=id)
    frm = RegiaoForm(request.POST or None, instance=regiao)

    if frm.is_valid():
        frm.save()
        return redirect('regioes.lista')
    
    return render(request, 'regioes/form.html', {
        'frm': frm,
        'titulo': 'Atualizar Regiao'
    })

def delete(request, id):
    regiao = get_object_or_404(Regiao, pk=id)
    regiao.delete()
    return redirect('regioes.lista')