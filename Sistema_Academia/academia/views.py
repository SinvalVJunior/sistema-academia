from django.shortcuts import render, redirect
from django.http import HttpResponse
from  django.contrib import messages
from django.contrib.auth.models import User
from .models import Academia_Users
from django.contrib.auth.forms import AuthenticationForm
from aluno.models import Aluno

def home(request):
    return render(request,'academia/home.html')

def login(request):

    if(request.method == 'POST'):
        data = request.POST.copy()

        username = data.get('username')
        if(data.get('tipo') == "Aluno"):
            user_found = Aluno.objects.filter(usuario=username).first()
            tipo = "aluno"
        else:
            user_found = Academia_Users.objects.filter(username=username).first()
            if(user_found):
                tipo = user_found.tipo.lower()
        if(user_found != None):
            if(user_found.password == data.get('password')):
                messages.success(request,f'Bem-vindo {username}! Você foi logado com sucesso!')
                request.session['user_logged_id'] = user_found.id
                return redirect(f'academia-{tipo}')
            else:
                messages.error(request,f'Nome ou usuario inválidos')
                return render(request,'academia/login.html')
        else:
            messages.error(request,f'Nome ou usuario inválidos')
            return render(request,'academia/login.html')

    return render(request,'academia/login.html')

def register(request):

    if(request.method == 'POST'):
        data = request.POST.copy()
        
        new_user = Academia_Users(username=data.get('usuario'),password=data.get('senha'),email=data.get('email'),tipo=data.get('tipo'))
        new_user.save()
        messages.success(request,f'Bem-vindo {data.get("usuario")}! Você foi registrado com sucesso!')
        return redirect('academia-home')

    return render(request,'academia/register.html')


def secretario(request):
    return render(request,'academia/secretario.html',{'username':"Teste"})