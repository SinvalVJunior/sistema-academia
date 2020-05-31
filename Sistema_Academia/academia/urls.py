from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='academia-home'),
    path('login',views.login,name='academia-login'),
    path('register',views.register,name='academia-register'),
    path('../secretario/home',views.secretario,name='academia-secretario'),
    path('../professor/home',views.secretario,name='academia-professor'),
    path('../medico/home',views.secretario,name='academia-medico'),
    path('../aluno/home',views.secretario,name='academia-aluno')
]