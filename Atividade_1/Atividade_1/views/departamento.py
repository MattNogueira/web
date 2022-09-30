from django.shortcuts import render, redirect, get_object_or_404
from Atividade_1.models import Departamento
from django.forms import ModelForm

class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'

def lista(request):
    return render(request, 'departamentos/lista.html', {
        'departamentos': Departamento.objects.all()
    })

def insert(request):
    frm = DepartamentoForm(request.POST or None)

    if frm.is_valid():
        frm.save()
        return redirect('departamentos.lista')
    
    return render(request, 'departamentos/form.html', {
        'frm': frm,
        'titulo': 'Cadastrar Departamento'
    })

def update(request, id):
    departamento = get_object_or_404(Departamento, pk=id)
    frm = DepartamentoForm(request.POST or None, instance=departamento)

    if frm.is_valid():
        frm.save()
        return redirect('departamentos.lista')
    
    return render(request, 'departamentos/form.html', {
        'frm': frm,
        'titulo': 'Atualizar Departamento'
    })

def delete(request, id):
    departamento = get_object_or_404(Departamento, pk=id)
    departamento.delete()
    return redirect('departamentos.lista')