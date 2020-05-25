from django.contrib import admin
from django.urls import path
from django.urls import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include('academia.urls'),name="home"),
    path('secretario/',include('secretario.urls'),name="secretario"),
    path('professor/',include('professor.urls'),name="professor")
]

urlpatterns += staticfiles_urlpatterns()