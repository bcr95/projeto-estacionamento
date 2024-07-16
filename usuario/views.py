from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_usuario
from django.contrib.auth.decorators import login_required
from rotativo.views import reservar

# Create your views here.
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
    
        verifica_usuario = User.objects.filter(username=username).first()

        if verifica_usuario:
            return HttpResponse('Nome de usuário já existente')
        
        usuario = User.objects.create_user(username=username, email=email, password=senha)
        usuario.save()
        
        return HttpResponse('Usuário cadastrado com sucesso')

def login(request):
    if  request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        autentica_usuario = authenticate(username=username, password=senha)

        if autentica_usuario:
            login_usuario(request, autentica_usuario)

            return redirect(reservar)
        else:
            return HttpResponse('Usuário ou senha inválidos')

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))