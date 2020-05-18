from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from academia.models import Academia_Users
from .models import *
from aluno.models import Aluno,Aula,Modalidade
from  django.contrib import messages


def home(request):
    user_id = request.session['user_logged_id']
    user = Academia_Users.objects.filter(id=user_id).first()
    '''
    #Script para adicionar aulas de acordo com o quadro de horarios
    aulas = Aula.objects.filter()
    for aula in aulas:
        if "Seg" in aula.name:
            new_name = aula.name.replace("Seg","Sex")
            new_day = "Sexta"
            new_aula = Aula(name=new_name,dia=new_day,horario=aula.horario)
            new_aula.save()
            modalidade = aula.name.rsplit()
            modalidade = Modalidade.objects.filter(name=modalidade[0]).first()
            new_aula.modalidade.add(modalidade)
            new_aula.save()
    '''
    return render(request,'secretario/home.html',{'user_logged':user})

def musculacao(request):
    user_id = request.session['user_logged_id']
    user = Academia_Users.objects.filter(id=user_id).first()

    plans = Plano.objects.filter()
    work_out_plans = []

    for plan in plans:
        if(plan.nome[0:10] == "Musculacao"):
            plan.nome = plan.nome[10:]
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
        if(plan.nome[0:7] == "Natacao"):
            plan.nome = plan.nome[7:]
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
        if(plan.nome[0:7] == "Variado"):
            plan.nome = plan.nome[7:]
            variade_plans.append(plan)

    context = {'user_logged':user,
                'plans': variade_plans
              }
    return render(request,'secretario/planos.html',context)


def matricular(request):
    plan_name=""
    if(request.method == "POST"):
        data = request.POST.copy()
        
        if(data.get("Musculacao Anual 7x na Semana")):
            plan_name="Musculacao Anual 7x na Semana"
        elif(data.get("Musculacao Semestral 7x na Semana")):
            plan_name="Musculacao Semestral 7x na Semana"
        elif(data.get("Musculacao Mensal 7x na Semana")):
            plan_name="Musculacao Mensal 7x na Semana"
        elif(data.get("Variado Anual 3x na Semana")):
            plan_name="Variado Anual 3x na Semana"
        elif(data.get("Variado Semestral 3x na Semana")):
            plan_name="Variado Semestral 3x na Semana"
        elif(data.get("Variado Mensal 3x na Semana")):
            plan_name="Variado Mensal 3x na Semana"
        elif(data.get("Natacao Anual 3x na Semana")):
            plan_name="Natacao Anual 3x na Semana"
        elif(data.get("Natacao Anual 2x na Semana")):
            plan_name="Natacao Anual 2x na Semana"
        elif(data.get("Natacao Semestral 3x na Semana")):
            plan_name="Natacao Semestral 3x na Semana"
        elif(data.get("Natacao Semestral 2x na Semana")):
            plan_name="Natacao Semestral 2x na Semana"   
        elif(data.get("Natacao Mensal 3x na Semana")):
            plan_name="Natacao Mensal 3x na Semana"   
        elif(data.get("Natacao Mensal 2x na Semana")):
            plan_name="Natacao Mensal 2x na Semana"   
        
        #plano = Plano.objects.filter(nome=plan_name).first()
        #new_aluno = Aluno(nome=data.get("nome"),CPF=data.get("CPF"),identidade=data.get("identidade"),nascimento=data.get("nascimento"),n_cartao=data.get("n_cartao"),bandeira=data.get("bandeira"),cartao_nome=data.get("nome_cartao"),usuario=data.get("usuario"),email=data.get("email"),senha=data.get("senha"))
        request.session['nome']=data.get("nome")
        request.session['CPF']=data.get("CPF")
        request.session['identidade']=data.get("identidade")
        request.session['nascimento']=data.get("nascimento")
        request.session['n_cartao']=data.get("n_cartao")
        request.session['bandeira']=data.get("bandeira")
        request.session['cartao_nome']=data.get("nome_cartao")
        request.session['usuario']=data.get("usuario")
        request.session['email']=data.get("email")
        request.session['senha']=data.get("senha")
        request.session['plano']=plan_name

        #new_aluno.save()
        #new_aluno.planos.add(plano)
        #new_aluno.save()

        return redirect('secretario-confirmacao')

    return render(request,'secretario/registro_aluno.html')

def confirmacao(request):

    if(request.method=="POST"):
            new_aluno = Aluno(nome=request.session['nome'],CPF=request.session['CPF'],identidade=request.session['identidade'],nascimento=request.session['nascimento'],n_cartao=request.session['n_cartao'],bandeira=request.session['bandeira'],cartao_nome=request.session['cartao_nome'],usuario=request.session['usuario'],email=request.session['email'],senha=request.session['plano'])

            plano = Plano.objects.filter(nome=request.session['plano']).first()

            new_aluno.save()
            new_aluno.planos.add(plano)
            new_aluno.save()


    context = {
        'nome' : request.session['nome'],
        'CPF' : request.session['CPF'],
        'identidade' : request.session['identidade'],
        'nascimento' : request.session['nascimento'],
        'n_cartao' : request.session['n_cartao'],
        'bandeira' : request.session['bandeira'],
        'cartao_nome' : request.session['cartao_nome'],
        'usuario' : request.session['usuario'],
        'email' : request.session['email'],
        'senha' : request.session['senha'],
        'plano' : request.session['plano']
    }
    return render(request,'secretario/confirmacao_dados.html',context)

def horarios(request):
    return render(request,'secretario/quadro_horarios.html')