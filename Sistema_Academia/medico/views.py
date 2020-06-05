from django.shortcuts import render,redirect
from academia.models import Academia_Users
from  django.contrib import messages
from aluno.models import *


def home(request):
    user_id = request.session['user_logged_id']
    user = Academia_Users.objects.filter(id=user_id).first()

    return render(request,'medico/home.html',{'user_logged':user})

def add_exame(request):
    user_id = request.session['user_logged_id']
    user = Academia_Users.objects.filter(id=user_id).first()

    if(request.method == "POST"):
        data = request.POST.copy()
        
        
        exame = Exame(cpf_aluno=data.get('Cpf'), peso=data.get('Peso'),altura=data.get('Altura'),pressao=data.get('Pressao'),pgc=data.get('PGC'),pmm=data.get('PMM'),imc=data.get('IMC'),habilitado=data.get('habilitado'),id_medico=user.id)
        exame.save()
        
        messages.success(request,"Cadastro de Exame realizado com sucesso !")

        return redirect('medico-home')
    return render(request,'medico/add_exame.html')