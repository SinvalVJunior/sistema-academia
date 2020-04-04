from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from academia.models import Academia_Users


def home(request):
    user_id = request.session['user_logged_id']
    user = Academia_Users.objects.filter(id=user_id).first()
    return render(request,'secretario/home.html',{'user_logged':user})

def musculacao(request):
    user_id = request.session['user_logged_id']
    user = Academia_Users.objects.filter(id=user_id).first()
    return render(request,'secretario/musculacao.html',{'user_logged':user})

def natacao(request):
    user_id = request.session['user_logged_id']
    user = Academia_Users.objects.filter(id=user_id).first()
    return render(request,'secretario/natacao.html',{'user_logged':user})

def variado(request):
    user_id = request.session['user_logged_id']
    user = Academia_Users.objects.filter(id=user_id).first()
    return render(request,'secretario/variado.html',{'user_logged':user})
