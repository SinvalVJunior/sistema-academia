from django.shortcuts import render,redirect
from academia.models import Academia_Users
from aluno.models import Aluno
from .models import Treino
from  django.contrib import messages


def home(request):
    user_id = request.session['user_logged_id']
    user = Academia_Users.objects.filter(id=user_id).first()

    return render(request,'professor/home.html',{'user_logged':user})

def lista_alunos(request):

    alunos = Aluno.objects.filter()

    if(request.method == "POST"):
        data = request.POST.copy()
        alunos_selecionados = []
        for aluno in alunos:
            if(data.get(f'{aluno.id}') == "on"):
                alunos_selecionados.append(aluno.id)
        
        request.session['alunos_selecionados'] = alunos_selecionados

        return redirect('professor-home')

    context = {
        "alunos": alunos,
    }

    
    return render(request,'professor/lista_alunos.html',context)

def criar_treino(request):

    alunos_selecionados = request.session['alunos_selecionados']

    alunos = []
    for aluno_id in alunos_selecionados:
        alunos.append(Aluno.objects.filter(id=int(aluno_id)).first())

    if(request.method == "POST"):
        data = request.POST.copy()
        user_id = request.session['user_logged_id']
        user = Academia_Users.objects.filter(id=user_id).first()


        for aluno in alunos:
            treino_nome="Aluno:"+aluno.nome+" Professor:"+user.username+" Treino"
            treino = Treino(nome=treino_nome, peito=data.get('peito'),costas=data.get('costas'),biceps=data.get('biceps'),triceps=data.get('triceps'),ombro=data.get('ombro'))
            treino.save()
            treino.professor.add(user)
            treino.save()
            aluno.treino.add(treino)
            aluno.save()

            messages.success(request,"Treino adicionado com sucesso!")

            redirect('professor-home')

            

    context = {
        'alunos': alunos,
    }
    return render(request,'professor/criar_treino.html',context)

def lista_treinos(request):
    user_id = request.session['user_logged_id']
    user = Academia_Users.objects.filter(id=user_id).first()

    treinos = Treino.objects.filter(professor=user)

    context = {
        "treinos": treinos,
    }
    
    return render(request,"professor/lista_treinos.html",context)

    
