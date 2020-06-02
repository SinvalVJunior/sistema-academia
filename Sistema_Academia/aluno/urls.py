from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='aluno-home'),
    path('view_exame/',views.view_exame,name='aluno-view_exame'),
    path('view_imc/',views.view_imc,name='aluno-view_imc')
]