from django.shortcuts import render, redirect
from .forms import NomeForm

def pagina_inicial(request):
    if request.method == 'POST':
        form = NomeForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            return redirect('saudacao', nome=nome)
    else:
        form = NomeForm()
    
    return render(request, 'saudacao/inicial.html', {'form': form})

def pagina_saudacao(request, nome):
    return render(request, 'saudacao/saudacao.html', {'nome': nome})