from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Rotativo

def cadastrar_rotativo(request):
    if request.method == 'GET':
        return render(request, 'cadastrar_rotativo.html')
    else:
        data = request.POST.get('data')
        hora_entrada = request.POST.get('hora_entrada')
        hora_saida = request.POST.get('hora_saida')

        rotativo = Rotativo(data=data, hora_entrada=hora_entrada, hora_saida=hora_saida)
        rotativo.save()

        return HttpResponse('Dados cadastrados com sucesso')
        
    
def listar_rotativo(request):
    lista = Rotativo.objects.all()
    return render(request, 'listar_rotativo.html', {'lista':lista})

def deletar_rotativo(request, id):
    lista = Rotativo.objects.get(id=id)
    lista.delete()
    return redirect(listar_rotativo)

def exibir_rotativo(request, id):
    lista = Rotativo.objects.get(id=id)
    return render(request, 'editar_rotativo.html', {'lista':lista})

def editar_rotativo(request, id):
    nova_data = request.POST.get("data")
    nova_hora_entrada = request.POST.get("hora_entrada")
    nova_hora_saida = request.POST.get("hora_saida")

    lista = Rotativo.objects.get(id=id)
    lista.data = nova_data
    lista.hora_entrada = nova_hora_entrada
    lista.hora_saida = nova_hora_saida
    lista.save()

    return redirect(listar_rotativo)