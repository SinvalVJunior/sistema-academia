from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='medico-home'),
    path('add_exame/',views.add_exame,name='medico-add_exame'),

]