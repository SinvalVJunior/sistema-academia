from django.shortcuts import render
from academia.models import Academia_Users


def home(request):
    user_id = request.session['user_logged_id']
    user = Academia_Users.objects.filter(id=user_id).first()

    return render(request,'professor/home.html',{'user_logged':user})
