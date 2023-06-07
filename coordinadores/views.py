from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Coordinador, coordinador_modificado, coordinador_inexistente
from .forms import CoordinadorForm


# Create your views here.
def modificar_coordinador(request, id):
    try:
        coordinador = Coordinador.objects.get(id=id)

        if request.method == 'POST':
            formulario = CoordinadorForm(request.POST, instance=coordinador)

            if formulario.is_valid():
                formulario.save()
                contexto = coordinador_modificado('modificado')
                return render(request, 'avisos.html', contexto)

        else:
            formulario = CoordinadorForm(instance=coordinador)

        contexto = {'formulario': formulario}

        return render(request, 'modificar_coordinador.html', contexto)

    except ObjectDoesNotExist:
        contexto = coordinador_inexistente(id)
        return render(request, 'avisos.html', contexto)
  
  
def listar_coordinadores(request):
    coordinadores = Coordinador.objects.all()
    contexto = {'coordinadores': coordinadores}

    return render(request, 'listar_coordinadores.html', contexto)


def agregar_coordinador(request):
    formulario = CoordinadorForm()
    if request.method == 'POST':
        formulario = CoordinadorForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            contexto = coordinador_modificado('agregado')
            return render(request, 'avisos.html', contexto)
        else:
            return HttpResponseRedirect('/coordinadores/agregar')
    contexto = {'formulario': formulario}

    return render(request, 'agregar_coordinador.html', contexto)


def activar_coordinador(request, id):
    contexto = dict()
    try:
        coordinador = Coordinador.objects.get(id=id)
        coordinador.activo = True
        coordinador.save()

        contexto = coordinador_modificado('activado')

    except ObjectDoesNotExist:
        contexto = coordinador_inexistente(id)

    finally:
        return render(request, 'avisos.html', contexto)


def desactivar_coordinador(request, id):
    contexto = dict()
    try:
        coordinador = Coordinador.objects.get(id=id)
        coordinador.activo = False
        coordinador.save()

        contexto = coordinador_modificado('desactivado')

    except ObjectDoesNotExist:
        contexto = coordinador_inexistente(id)

    finally:
        return render(request, 'avisos.html', contexto)
