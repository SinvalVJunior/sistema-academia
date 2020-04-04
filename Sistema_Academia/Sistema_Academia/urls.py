from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include('academia.urls')),
    path('secretario/',include('secretario.urls'),name="secretario")

]
