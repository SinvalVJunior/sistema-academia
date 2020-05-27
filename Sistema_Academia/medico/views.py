from django.shortcuts import render,redirect
from academia.models import Academia_Users
from  django.contrib import messages
from aluno.models import *


def home(request):
    user_id = request.session['user_logged_id']
    user = Academia_Users.objects.filter(id=user_id).first()

    return render(request,'medico/home.html',{'user_logged':user})

def lista_alunos(request):

    alunos = Aluno.objects.filter()

    if(request.method == "POST"):
        data = request.POST.copy()
        alunos_selecionados = []
        for aluno in alunos:
            if(data.get(f'{aluno.id}') == "on"):
                alunos_selecionados.append(aluno.id)
        if(len(alunos_selecionados)>1):
                messages.error(request,"Selecione somente um aluno!")
                return redirect('medico-lista_alunos')

        request.session['alunos_selecionados'] = alunos_selecionados

        return redirect('medico-add_exame')

    context = {
        "alunos": alunos,
    }

    
    return render(request,'medico/lista_alunos.html',context)


def add_exame(request):
    user_id = request.session['user_logged_id']
    user = Academia_Users.objects.filter(id=user_id).first()

    if(request.method == "POST"):
        data = request.POST.copy()
        aluno = Aluno.objects.filter(id=request.session['alunos_selecionados'][0]).first()
        
        exame = Exame(id_aluno=aluno.id, peso=data.get('Peso'),altura=data.get('Altura'),pressao=data.get('Pressao'),pgc=data.get('PGC'),pmm=data.get('PMM'),imc=data.get('IMC'),habilitado=data.get('habilitado'),id_medico=user.id)
        exame.save()
        aluno.exame.add(exame)
        aluno.save()
        messages.success(request,"Cadastro de Exame realizado com sucesso !")

        return redirect('medico-home')
    return render(request,'medico/add_exame.html')