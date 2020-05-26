from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='professor-home'),
    path('lista_alunos/',views.lista_alunos,name='professor-lista_alunos'),
    path('criar_treino/',views.criar_treino,name='professor-criar_treino')


]