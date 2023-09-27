from django.shortcuts import render
from .models import users

def home(request):
    return render(request, 'usuarios/home.html')


def usuarios(request):
    newUser = users()
    newUser.name = request.POST.get('name')
    newUser.idade = request.POST.get('age')
    newUser.save()

    #SHOW ALL THE USERS ON A NEW PAGE

    usuarios = {
         'usuarios': users.objects.all()
    }

    #RETURNING DATA TO THE LISTING PAGE
    return render(request,'usuarios/usuarios.html', usuarios)

   