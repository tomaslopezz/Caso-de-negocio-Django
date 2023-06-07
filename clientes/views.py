from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Cliente, cliente_modificado, cliente_inexistente
from .forms import ClienteForm


# Create your views here.
def agregar_cliente(request):
    formulario = ClienteForm()
    if request.method == 'POST':
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            contexto = cliente_modificado('agregado')
            return render(request, 'avisos.html', contexto)
        else:
            return HttpResponseRedirect('/clientes/listar')
    contexto = {'formulario': formulario}
    return render(request, 'agregar_cliente.html', contexto)


def listar_clientes(request):
    clientes = Cliente.objects.all()
    contexto = {'clientes': clientes}

    return render(request, 'listar_clientes.html', contexto)


def activar_cliente(request, id):
    contexto = dict()
    try:
        cliente = Cliente.objects.get(id=id)
        cliente.activo = True
        cliente.save()

        contexto = cliente_modificado('activado')

    except ObjectDoesNotExist:
        contexto = cliente_inexistente(id)

    finally:
        return render(request, 'avisos.html', contexto)


def desactivar_cliente(request, id):
    contexto = dict()
    try:
        cliente = Cliente.objects.get(id=id)
        cliente.activo = False
        cliente.save()

        contexto = cliente_modificado('desactivado')

    except ObjectDoesNotExist:
        contexto = cliente_inexistente(id)

    finally:
        return render(request, 'avisos.html', contexto)


def modificar_cliente(request, id):
    try:
        cliente = Cliente.objects.get(id=id)

        if request.method == 'POST':
            formulario = ClienteForm(request.POST, instance=cliente)

            if formulario.is_valid():
                formulario.save()
                contexto = cliente_modificado('modificado')
                return render(request, 'avisos.html', contexto)
        else:
            formulario = ClienteForm(instance=cliente)

        contexto = {'formulario': formulario}
        return render(request, 'modificar_cliente.html', contexto)

    except ObjectDoesNotExist:
        contexto = cliente_inexistente(id)
        return render(request, 'avisos.html', contexto)
