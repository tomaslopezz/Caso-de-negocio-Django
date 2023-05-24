from django.shortcuts import render
from .models import Cliente

# Create your views here.
def listar_clientes(request):
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}

    return render(request, 'lista_clientes.jinja', context)
