from typing import List
from rest_framework import serializers
from todo_app.models import ListaTarefas, Tarefa
from todo_app.utils import StatusTarefa


class ListaTarefasSerializer(serializers.ModelSerializer):
    tarefas = serializers.PrimaryKeyRelatedField(many=True, queryset=Tarefa.objects.all())

    class Meta:
        model = ListaTarefas
        fields = ['id', 'nome_lista', 'data_criacao', 'tarefas']

    def create(self, lista_tarefas):
        tarefas = lista_tarefas.pop('tarefas')
        lista = ListaTarefas.objects.create(**lista_tarefas)
        lista.tarefas.set(tarefas)
        lista.save()
        return lista
    
    def update(self, lista_tarefas, nova_lista_tarefas):
        lista_tarefas.nome_lista = nova_lista_tarefas.get('nome_lista')
        lista_tarefas.data_criacao = nova_lista_tarefas.get('data_criacao')
        tarefas = nova_lista_tarefas.pop('tarefas')
        lista_tarefas.tarefas.set(tarefas)
        lista_tarefas.save()
        return lista_tarefas


class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = ['id', 'lista_tarefas', 'descricao', 'data_criacao', 'status']

    def create(self, tarefa):
        return Tarefa.objects.create(**tarefa)
    
    def update(self, tarefa, nova_tarefa):
        tarefa.lista_tarefas = nova_tarefa.get('lista_tarefas')
        tarefa.descricao = nova_tarefa.get('descricao')
        tarefa.data_criacao = nova_tarefa.get('data_criacao')
        tarefa.status = nova_tarefa.get('status')
        tarefa.save()

        return tarefa