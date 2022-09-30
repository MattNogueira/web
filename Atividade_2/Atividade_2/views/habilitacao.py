from django.shortcuts import redirect, render, get_object_or_404
from Atividade_2.models import Habilitacao
from django.forms import ModelForm

class HabilitacaoForm(ModelForm):
    class Meta:
        model = Habilitacao
        fields = '__all__'

def lista(request):
    return render(request, 'habilitacoes/lista.html', {
        'habilitacoes': Habilitacao.objects.all()
    })

def insert(request):
    frm = HabilitacaoForm(request.POST or None)

    if frm.is_valid():
        frm.save()
        return redirect('habilitacoes.lista')
    
    return render(request, 'habilitacoes/form.html', {
        'frm':frm,
        'titulo': 'Cadastrar Habilitação'
    })

def update(request, id):
    habilitacao = get_object_or_404(Habilitacao, pk=id)
    frm = HabilitacaoForm(request.POST or None, instance=habilitacao)

    if frm.is_valid():
        frm.save()
        return redirect('habilitacoes.lista')

    return render(request, 'hablitacoes/form.html', {
        'frm': frm,
        'titulo':'Atualizar Habilitação'
    })

def delete(request, id):
    habilitacao = get_object_or_404(Habilitacao, pk=id)
    habilitacao.delete()
    return redirect('habilitacoes.lista')