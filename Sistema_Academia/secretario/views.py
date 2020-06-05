from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from academia.models import Academia_Users
from .models import *
from aluno.models import Aluno,Aula,Modalidade
from  django.contrib import messages
from medico.models import Exame


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

def matricular(request):
    plan_name=""
    if(request.method == "POST"):
        data = request.POST.copy()
                
        if data.get("modalidade") == "nselecionado":
            messages.error(request,"Selecione uma modalidade")
            return render(request,'secretario/registro_aluno.html')

        modalidades = []
        modalidades.append(data.get("modalidade"))

        aux = 0
        while (data.get(f'modalidade{aux}')):
            if data.get(f'modalidade{aux}') == "nselecionado":
                messages.error(request,"Selecione uma modalidade")
                return render(request,'secretario/registro_aluno.html')
            if(data.get(f'modalidade{aux}') not in modalidades):
                modalidades.append(data.get(f'modalidade{aux}'))
            aux+=1
        
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
        request.session['modalidades']=modalidades

        return redirect('secretario-lista_planos')

    return render(request,'secretario/registro_aluno.html')

def lista_planos(request):

    if request.method == "POST":
        data = request.POST.copy()
        all_planos = Plano.objects.filter()
        planos_selecionados = []
        
        for plano in all_planos:
            if(data.get(f'{plano.id}')):
                planos_selecionados.append(plano.id)

        request.session['planos'] = planos_selecionados
        return redirect('secretario-lista_aulas')

    modalidades = request.session['modalidades']
    planos = []
    for modalidade in modalidades:
        planos.append(Plano.objects.filter(modalidade=modalidade))

    context = {
        'planosDisponiveis':planos
    }
    return render(request,'secretario/lista_planos.html',context)

def lista_aulas(request):
    all_aulas = Aula.objects.filter()
    aulas_selecionadas = []

    if request.method == "POST":
        data = request.POST.copy() 
        
        for aula in all_aulas:
            if data.get(f'{aula.id}'):
                aulas_selecionadas.append(aula.id)
        request.session['aulas'] = aulas_selecionadas

        return redirect('secretario-view_exame')

        
    aulas = []
    aulas_plano = []
    for plano_id in request.session['planos']:
        plano = Plano.objects.filter(id=plano_id).first()
        modalidades = [plano.modalidade.capitalize()]
        if modalidades == ["Variado"]:
            modalidades = ["Spinning","Crossfit","Ritmos"]
        for modalidade in modalidades:
            aulas_plano = []
            for aula in all_aulas:
                if(aula.modalidade.get().name in modalidade):
                    aulas_plano.append(aula)
            if aulas_plano:
                aulas.append(aulas_plano)
    
    context = {
        'aulasDisponiveis': aulas
    }
    return render(request,'secretario/lista_aulas.html',context)

def view_exame(request):
    cpf = request.session['CPF']

    exames = Exame.objects.filter(cpf_aluno=cpf)

    if request.method == "POST":
        data = request.POST.copy()
        request.session['exame'] = exames[0].id 
        if data.get('confirmacao'):
            return redirect('secretario-confirmacao')
        else:
            messages.error(request,"Leia o Exame de Aptidão e marque a confirmação de leitura")
        
    
    context = {
        'exames':exames,
        'cpf':cpf
    }
    return render(request,'secretario/view_exame.html',context)

def confirmacao(request):
    planos = []
    for plano_id in request.session['planos']:
        planos.append(Plano.objects.filter(id=plano_id).first())

    aulas = []
    for aula_id in request.session['aulas']:
        aulas.append(Aula.objects.filter(id=aula_id).first())

    if(request.method=="POST"):
            new_aluno = Aluno(nome=request.session['nome'],CPF=request.session['CPF'],identidade=request.session['identidade'],nascimento=request.session['nascimento'],n_cartao=request.session['n_cartao'],bandeira=request.session['bandeira'],cartao_nome=request.session['cartao_nome'],usuario=request.session['usuario'],email=request.session['email'],password=request.session['senha'])
            new_aluno.save()

            for plano in planos:
                new_aluno.planos.add(plano)
            new_aluno.save()

            for aula in aulas:
                aula.alunos.add(new_aluno)
                aula.save()

            exame = Exame.objects.filter(id=f'{request.session["exame"]}').first()
            new_aluno.exame.add(exame)
            new_aluno.save()

            messages.success(request,"Aluno Matriculado com Sucesso !! Bem vindo à Academia")
            
            return redirect('secretario-home')

    

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
        'planos' : planos,
        'aulas': aulas
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
