from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ClienteForm

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
