from django.urls import path
from . import views


urlpatterns = [
    path('home/',views.home,name='secretario-home'),
    path('musculacao/',views.musculacao,name='secretario-musculacao'),
    path('natacao/',views.natacao,name='secretario-natacao'),
    path('variado/',views.variado,name='secretario-variado')

]
