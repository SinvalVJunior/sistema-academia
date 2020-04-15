from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from academia.models import Academia_Users
from .models import *
from aluno.models import Aluno

def home(request):
    user_id = request.session['user_logged_id']
    user = Academia_Users.objects.filter(id=user_id).first()
    return render(request,'secretario/home.html',{'user_logged':user})

def musculacao(request):
    user_id = request.session['user_logged_id']
    user = Academia_Users.objects.filter(id=user_id).first()

    plans = Plano.objects.filter()
    work_out_plans = []

    for plan in plans:
        if(plan.name[0:10] == "Musculacao"):
            plan.name = plan.name[10:]
            work_out_plans.append(plan)

    context = {'user_logged':user,
                'plans': work_out_plans
              }

    return render(request,'secretario/planos.html',context)

def natacao(request):

    user_id = request.session['user_logged_id']
    user = Academia_Users.objects.filter(id=user_id).first()

    plans = Plano.objects.filter()
    swimming_plans = []

    for plan in plans:
        if(plan.name[0:7] == "Natacao"):
            plan.name = plan.name[7:]
            swimming_plans.append(plan)

    context = {'user_logged':user,
                'plans': swimming_plans
              }
    return render(request,'secretario/planos.html',context)

def variado(request):
    user_id = request.session['user_logged_id']
    user = Academia_Users.objects.filter(id=user_id).first()

    plans = Plano.objects.filter()
    variade_plans = []

    for plan in plans:
        if(plan.name[0:7] == "Variado"):
            plan.name = plan.name[7:]
            variade_plans.append(plan)

    context = {'user_logged':user,
                'plans': variade_plans
              }
    return render(request,'secretario/planos.html',context)


def matricular(request):

    if(request.method == "POST"):
        data = request.POST.copy()
        
        #new_aluno = Aluno(data.get('usuario'))
    return render(request,'secretario/registro_aluno.html')
