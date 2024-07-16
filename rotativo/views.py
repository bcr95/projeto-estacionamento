from django.shortcuts import render, redirect
from .models import Reserva
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/auth/login/")
def reservar(request):
    reservas = Reserva.objects.all()
    return render(request, 'cadastro_reservas.html', {'reservas':reservas})

@login_required(login_url="/auth/login/")
def salvar(request):
    nova_data = request.POST.get('data')
    nova_hora_entrada = request.POST.get('hora_entrada')
    nova_hora_saida = request.POST.get('hora_saida')
    reserva = Reserva.objects.create(data=nova_data, hora_entrada=nova_hora_entrada, hora_saida=nova_hora_saida)
    reserva.save()

    return redirect(reservar)

@login_required(login_url="/auth/login/")
def listar(request):
    reservas = Reserva.objects.all()
    return render(request, 'reservas.html', {'reservas':reservas})

@login_required(login_url="/auth/login/")
def editar(request, id):
    reserva = Reserva.objects.get(id=id)
    return render(request, 'update.html', {'reserva':reserva})

@login_required(login_url="/auth/login/")
def update(request, id):
    nova_data = request.POST.get('data')
    nova_hora_entrada = request.POST.get('hora_entrada')
    nova_hora_saida = request.POST.get('hora_saida')
    reserva = Reserva.objects.get(id=id)
    reserva.data = nova_data
    reserva.hora_entrada = nova_hora_entrada
    reserva.hora_saida = nova_hora_saida
    reserva.save()
    return redirect(reservar)

@login_required(login_url="/auth/login/")
def excluir(request, id):
    reserva = Reserva.objects.get(id=id)
    reserva.delete()
    return redirect(reservar)