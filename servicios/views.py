from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, HttpResponse
from .models import Servicio
from .forms import ServicioForm


# Create your views here.

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

        contexto = {'formulario': formulario}

        return render(request, 'modificar_servicio.html', contexto)

    except ObjectDoesNotExist as e:
        return HttpResponse("<h1>Servicio inexistente</h1>")
