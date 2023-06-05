from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Servicio, servicio_modificado, servicio_inexistente
from .forms import ServicioForm


# Create your views here.
def agregar_servicio(request):
    formulario = ServicioForm()
    if request.method == 'POST':
        formulario = ServicioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            contexto = servicio_modificado('agregado')
            return render(request, 'avisos.html', contexto)
        else:
            return HttpResponseRedirect('/servicios/agregar')
    contexto = {'formulario': formulario}
    return render(request, 'agregar_servicio.html', contexto)


def listar_servicios(request):
    servicios = Servicio.objects.all()
    contexto = {'servicios': servicios}
    return render(request, 'listar_servicios.html', contexto)


def activar_servicio(request, id):
    contexto = dict()
    try:
        servicio = Servicio.objects.get(id=id)
        servicio.activo = True
        servicio.save()

        contexto = servicio_modificado('activado')

    except ObjectDoesNotExist:
        contexto = servicio_inexistente(id)

    finally:
        return render(request, 'avisos.html', contexto)


def desactivar_servicio(request, id):
    contexto = dict()
    try:
        servicio = Servicio.objects.get(id=id)
        servicio.activo = False
        servicio.save()

        contexto = servicio_modificado('desactivado')

    except ObjectDoesNotExist:
        contexto = servicio_inexistente(id)

    finally:
        return render(request, 'avisos.html', contexto)


def modificar_servicio(request, id):
    try:
        servicio = Servicio.objects.get(id=id)

        if request.method == 'POST':
            formulario = ServicioForm(request.POST, instance=servicio)

            if formulario.is_valid():
                formulario.save()
                contexto = servicio_modificado('modificado')
                return render(request, 'avisos.html', contexto)

        else:
            formulario = ServicioForm(instance=servicio)

        contexto = {'formulario': formulario}

        return render(request, 'modificar_servicio.html', contexto)

    except ObjectDoesNotExist:
        contexto = servicio_inexistente(id)
        return render(request, 'avisos.html', contexto)
