
from django.urls import path
from app_register import views


urlpatterns = [
    #rota, view e nome de referência
    path('', views.home,name='home'),
    path('users/', views.usuarios, name='listagem_usuarios')
]