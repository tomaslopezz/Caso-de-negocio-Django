from django.shortcuts import render, HttpResponse
from .models import Cliente

# Create your views here.
def activar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.activo = True
    cliente.save()
    return HttpResponse("<h1>Cliente activado con exito</h1>")