from django.shortcuts import render
from academia.models import Academia_Users 
from .models import Aluno,Aula

def home(request):
    user_id = request.session['user_logged_id']
    user = Aluno.objects.filter(id=user_id).first()
    
    try:
        treino = user.treino.get()
    except:
        treino = None


    all_aulas = Aula.objects.filter()
    aulas_aluno = []

    for aula in all_aulas:
        if(user in aula.alunos.all()):
            aulas_aluno.append(aula)
    
    horarios = []
    for aula in aulas_aluno:
        if aula.horario not in horarios:
            horarios.append(aula.horario)

    horarios.sort()
    tabela = []
    dias_uteis = ["Seg", "Ter", "Qua", "Qui", "Sex"]
    has_aula = False
    for horario in horarios:
        aulas_do_dia = []
        for dia in dias_uteis:
            has_aula = False
            for aula in aulas_aluno:
                if dia in aula.dia and horario in aula.horario:
                    aulas_do_dia.append(aula)
                    has_aula = True
            if not has_aula:
                aulas_do_dia.append([])

    
        tabela.append(aulas_do_dia)
            
    context = {
        'user_logged': user,
        'treino': treino,
        'has_aula': len(aulas_aluno),
        'horarios': horarios,
        'tabela': tabela,
    }
    return render(request,'aluno/home.html',context)
