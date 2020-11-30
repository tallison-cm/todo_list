from django.db import models
from .utils import StatusTarefa
from datetime import datetime


class ListaTarefas(models.Model):
    nome_lista = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return self.nome_lista


class Tarefa(models.Model):
    lista_tarefas = models.ForeignKey(ListaTarefas, related_name='tarefas', on_delete=models.CASCADE, blank=True, null=True)
    descricao = models.CharField(max_length=300)
    data_criacao = models.DateTimeField(default=datetime.now())
    status = models.IntegerField(choices=StatusTarefa.choices(), default=StatusTarefa.NAO_CONCLUIDA)

    def __str__(self):
        return self.descricao