from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from .forms import ClienteForm
from .models import Cliente

# Create your views here.

def agregar_cliente(request):
    formulario = ClienteForm()
    if request.method == 'POST':
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            return HttpResponseRedirect('/agregar_cliente/')
    contexto = {
        'formulario' : formulario
    }
    return render(request, 'agregar_cliente.jinja', context=contexto)

  
def activar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.activo = True
    cliente.save()
    return HttpResponse("<h1>Cliente activado con exito</h1>")
