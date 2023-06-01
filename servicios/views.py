from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from .models import Servicio
from .forms import ServicioForm


# Create your views here.
def agregar_servicio(request):
    formulario = ServicioForm()
    if request.method == 'POST':
        formulario = ServicioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            return HttpResponseRedirect('/agregar_servicio/')
    contexto = {
        'formulario': formulario
    }
    return render(request, 'agregar_servicio.html', context=contexto)


def activar_servicio(request, id):
    try:
        servicio = Servicio.objects.get(id=id)
        servicio.activo = True
        servicio.save()
        return HttpResponse("<h1>Servicio activado con exito</h1>")
    except ObjectDoesNotExist as e:
        return HttpResponse("<h1>Servicio inexistente</h1>")


def modificar_servicio(request, id):
    try:
        servicio = Servicio.objects.get(id=id)

        if request.method == 'POST':
            formulario = ServicioForm(request.POST, instance=servicio)

            if formulario.is_valid():
                formulario.save()
                return HttpResponse("<h1>Servicio modificado con exito</h1>")

        else:
            formulario = ServicioForm(instance=servicio)

        context = {'formulario': formulario}

        return render(request, 'modificar_servicio.html', context)

    except ObjectDoesNotExist as e:
        return HttpResponse("<h1>Servicio inexistente</h1>")
