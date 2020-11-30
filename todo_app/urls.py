from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('listas/', views.ListaTarefasList.as_view()),
    path('lista/<int:pk>/', views.ListaTarefasDetail.as_view()),
    path('tarefas/', views.TarefaList.as_view()),
    path('tarefa/<int:pk>/', views.TarefaDetail.as_view()),
]

#urlpatterns = format_suffix_patterns(urlpatterns)