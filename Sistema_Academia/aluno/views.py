from django.shortcuts import render
from academia.models import Academia_Users 
from .models import Aluno

def home(request):
    user_id = request.session['user_logged_id']
    user = Aluno.objects.filter(id=user_id).first()
    return render(request,'aluno/home.html',{'user_logged':user})
