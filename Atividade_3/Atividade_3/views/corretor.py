from django.shortcuts import render, redirect, get_object_or_404
from Atividade_3.models import Corretor
from django.forms import ModelForm

class CorretorForm(ModelForm):
    class Meta:
        model = Corretor
        fields = '__all__'

def lista(request):
    return render(request, 'corretores/lista.html', {
        'corretores': Corretor.objects.all()
    })

def insert(request):
    frm = CorretorForm(request.POST or None)

    if frm.is_valid():
        frm.save()
        return redirect('corretores.lista')
    
    return render(request, 'corretores/form.html', {
        'frm': frm,
        'titulo': 'Cadastrar Corretores'
    })

def update(request, id):
    corretor = get_object_or_404(Corretor, pk=id)
    frm = CorretorForm(request.POST or None, instance=corretor)

    if frm.is_valid():
        frm.save()
        return redirect('corretores.lista')
    
    return render(request, 'corretores/form.html', {
        'frm': frm,
        'titulo': 'Atualizar Corretor'
    })

def delete(request, id):
    corretor = get_object_or_404(Corretor, pk=id)
    corretor.delete()
    return redirect('corretores.lista')