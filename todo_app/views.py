from todo_app.models import ListaTarefas, Tarefa
from todo_app.serializers import ListaTarefasSerializer, TarefaSerializer
from rest_framework import generics


class ListaTarefasList(generics.ListCreateAPIView):
    queryset = ListaTarefas.objects.all()
    serializer_class = ListaTarefasSerializer

class ListaTarefasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ListaTarefas.objects.all()
    serializer_class = ListaTarefasSerializer


class TarefaList(generics.ListCreateAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

class TarefaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer