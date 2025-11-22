from django.urls import path
from . import views

urlpatterns = [
    # Rota principal (ex: http://127.0.0.1:8000/)
    path('', views.lista_tarefas, name='lista_tarefas'),
    
    # Rota para atualizar (marcar/desmarcar) uma tarefa
    # ex: /atualizar/5/
    path('atualizar/<int:pk>/', views.atualizar_tarefa, name='atualizar_tarefa'),
    
    # Rota para deletar uma tarefa
    # ex: /deletar/5/
    path('deletar/<int:pk>/', views.deletar_tarefa, name='deletar_tarefa'),
]