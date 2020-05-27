from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='medico-home'),
    path('lista_alunos/',views.lista_alunos,name='medico-lista_alunos'),
    path('add_exame/',views.add_exame,name='medico-add_exame'),

]