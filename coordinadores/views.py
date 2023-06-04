from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from .models import Coordinador
from .forms import CoordinadorForm


# Create your views here.
def modificar_coordinador(request, id):
    try:
        coordinador = Coordinador.objects.get(id=id)

        if request.method == 'POST':
            formulario = CoordinadorForm(request.POST, instance=coordinador)

            if formulario.is_valid():
                formulario.save()
                return HttpResponse("<h1>Coordinador modificado con exito</h1>")

        else:
            formulario = CoordinadorForm(instance=coordinador)

        contexto = {'formulario': formulario}

        return render(request, 'modificar_coordinador.html', contexto)

    except ObjectDoesNotExist as e:
        return HttpResponse("<h1>Coordinador inexistente</h1>")
  
  
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
        else:
            return HttpResponseRedirect('/coordinadores/agregar')
    contexto = {'formulario': formulario}

    return render(request, 'agregar_coordinador.html', contexto)


def activar_coordinador(request, id):
    try:
        coordinador = Coordinador.objects.get(id=id)
        coordinador.activo = True
        coordinador.save()
        return HttpResponse("<h1>Coordinador activado con exito</h1>")
    except ObjectDoesNotExist as e:
        return HttpResponse("<h1>Coordinador inexistente</h1>")


def desactivar_coordinador(request, id):
    coordinador = Coordinador.objects.get(id=id)
    coordinador.activo = False
    coordinador.save()
    return HttpResponse("<h1>Coordinador desactivado con exito</h1>")
