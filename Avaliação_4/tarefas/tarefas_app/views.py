from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Tarefa

def lista_tarefas(request):
    # Se a requisição for POST, significa que o formulário de "Nova Tarefa" foi enviado
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        if titulo: # Só cria se o título não estiver vazio
            Tarefa.objects.create(titulo=titulo)
        return redirect('lista_tarefas') # Redireciona para a mesma página (GET)

    # Se for GET, apenas buscamos e exibimos as tarefas
    tarefas_pendentes = Tarefa.objects.filter(concluida=False).order_by('-data_criacao')
    tarefas_concluidas = Tarefa.objects.filter(concluida=True).order_by('data_criacao')
    
    context = {
        'tarefas_pendentes': tarefas_pendentes,
        'tarefas_concluidas': tarefas_concluidas,
    }
    return render(request, 'tarefas_app/lista_tarefas.html', context)


# Garante que esta view só possa ser acessada via POST (pelo formulário)
@require_POST
def atualizar_tarefa(request, pk):
    # Busca a tarefa pelo ID (pk) ou retorna erro 404 se não existir
    tarefa = get_object_or_404(Tarefa, pk=pk)
    
    # Inverte o status de 'concluida'
    # Se era False, vira True. Se era True, vira False.
    tarefa.concluida = not tarefa.concluida
    tarefa.save()
    
    return redirect('lista_tarefas')


# Garante que esta view só possa ser acessada via POST
@require_POST
def deletar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    tarefa.delete()
    return redirect('lista_tarefas')
