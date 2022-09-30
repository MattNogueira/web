from django.shortcuts import render, redirect, get_object_or_404
from Atividade_3.models import Municipio
from django.forms import ModelForm

class MunicipioForm(ModelForm):
    class Meta:
        model = Municipio
        fields = '__all__'

def lista(request):
    return render(request, 'municipios/lista.html', {
        'municipios': Municipio.objects.all()
    })

def insert(request):
    frm = MunicipioForm(request.POST or None)

    if frm.is_valid():
        frm.save()
        return redirect('municipios.lista')

    return render(request, 'municipios/form.html', {
        'frm': frm,
        'titulo': 'Cadastrar Município'
    })

def update(request, id):
    municipio = get_object_or_404(Municipio, pk=id)
    frm = MunicipioForm(request.POST or None, instance=municipio)

    if frm.is_valid():
        frm.save()
        return redirect('municipios.lista')

    return render(request, 'municipios/form.html', {
        'frm': frm,
        'titulo': 'Atualizar Município'
    })

def delete(request, id):
    municipio = get_object_or_404(Municipio, pk=id)
    municipio.delete()
    return redirect('municipios.lista')