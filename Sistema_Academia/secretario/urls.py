from django.urls import path
from . import views


urlpatterns = [
    path('home/',views.home,name='secretario-home'),
    path('musculacao/',views.musculacao,name='secretario-musculacao'),
    path('natacao/',views.natacao,name='secretario-natacao'),
    path('variado/',views.variado,name='secretario-variado'),
    path('matricular/',views.matricular,name='secretario-matricular'),
    path('confirmacao/',views.confirmacao,name='secretario-confirmacao'),
    path('horarios/',views.horarios,name='secretario-horarios'),
    path('aula/',views.aula_perfil,name='secretario-aula'),
    path('adicionar_aluno/',views.add_aluno,name='secretario-add'),
    path('lista_planos/',views.lista_planos,name='secretario-lista_planos'),
    path('lista_aulas/',views.lista_aulas,name='secretario-lista_aulas'),
    path('view_exame/',views.view_exame,name='secretario-view_exame'),

]
