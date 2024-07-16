from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def cadastrar_cliente(request):
    if request.method == 'GET':
        return render(request, 'cadastrar_cliente.html')
    else:
        nome_usuario = request.POST.get('nome_usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        # Verificando se há outro usuário cadastrado com o mesmo nome
        user = User.objects.filter(username=nome_usuario).first()

        if user:
            return HttpResponse('Já existe um usuário com este nome')

        # Criando um novo usuário
        usuario = User.objects.create_user(username=nome_usuario, email=email, password=senha)
        usuario.save()

        return HttpResponse('Usuário cadastrado com sucesso')
    
def login_cliente(request):
    if request.method == 'GET':
        return render(request, 'login_cliente.html')
    else:
        nome_usuario = request.POST.get('nome_usuario')
        senha = request.POST.get('senha')

        user = authenticate(username=nome_usuario, password=senha)

        # Login permitido apenas se o usuário e a senha estiverem cadastrados no banco 
        if user:
            login(request, user)
            return render(request, 'cadastrar_rotativo.html')
        else:
            return HttpResponse('Usuário ou senha inválidos')

