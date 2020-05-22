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
    #Script para adicionar aulas de acordo com o quadro de horarios considerando que um dia ja foi adicionado
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

    selecionado = request.GET.get('modalidade','Crossfit')

    modalidade_selecionada = Modalidade.objects.filter(name=selecionado).first()
    all_aulas = Aula.objects.filter(modalidade=modalidade_selecionada)
    horarios = []
    tabela = []
    dias_uteis = ["Seg", "Ter", "Qua", "Qui", "Sex"]

    for aula in all_aulas:
        if aula.horario not in horarios:
            horarios.append(aula.horario)

    horarios.sort()
    for horario in horarios:
        aulas_do_dia = []
        for dia in dias_uteis:
            for aula in all_aulas:
                if dia in aula.dia and horario in aula.horario:
                    aulas_do_dia.append(aula)
        tabela.append(aulas_do_dia)
    
    context = {
        "horarios": horarios,
        "tabela": tabela,
        "modalidade": selecionado
    }

    return render(request,'secretario/quadro_horarios.html',context)
def aula_perfil(request):
    user_id = request.session['user_logged_id']
    secretario = Academia_Users.objects.filter(id=user_id).first()
    
    if secretario == None:
        return redirect('home')
    
    aula = Aula.objects.filter(id=request.GET.get("aula_id","0")).first()
    alunos = aula.alunos.all()
    context = {'user_logged':secretario,
                'aula':aula,
                'alunos':alunos
              }
    return render(request,"secretario/aula_perfil.html",context)

def add_aluno(request):

    
        
    aula = Aula.objects.filter(id=request.GET.get("aula_id","0")).first()
    alunos_inscritos = aula.alunos.all()
    alunos_matriculados = Aluno.objects.filter()
    alunos_possiveis = []

    for aluno in alunos_matriculados:
        if aluno not in alunos_inscritos:
            alunos_possiveis.append(aluno)

    if(request.method == "POST"):
        data = request.POST.copy()

        for aluno in alunos_possiveis:
            if(data.get(f'{aluno.id}') == "on"):
                aula.alunos.add(aluno)

        aula.save()
        messages.success(request,"Usuário(s) inscrito(s) com sucesso")


        return redirect("secretario-horarios")

    context = {
        "alunos":alunos_possiveis,
        "aula":aula
    }

    return render(request,"secretario/add_aluno.html",context)
    


