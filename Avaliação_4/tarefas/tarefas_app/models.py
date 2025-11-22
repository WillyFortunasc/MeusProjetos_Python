from django.db import models

class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    # blank=True e null=True tornam este campo opcional
    descricao = models.TextField(blank=True, null=True) 
    concluida = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Isso é o que aparecerá no painel Admin
        return self.titulo
    
    class Meta:
        # Ordena as tarefas pela data de criação por padrão
        ordering = ['data_criacao']