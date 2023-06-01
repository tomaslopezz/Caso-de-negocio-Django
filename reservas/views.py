from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from .forms import ReservaForm
from .models import Reserva


# Create your views here.
def agregar_reserva(request):
    if request.method == 'POST':
        formulario = ReservaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            return HttpResponseRedirect('/agregar_reserva/')

    else:
        formulario = ReservaForm()

    contexto = {'formulario': formulario}

    return render(request, 'agregar_reserva.html', context=contexto)

def listar_reservas(request):
    reservas = Reserva.objects.all()
    context = {'reservas': reservas}
    return render(request, 'listar_reservas.html', context)

def modificar_reserva(request, id):
    try:
        reserva = Reserva.objects.get(id=id)

        if request.method == 'POST':
            formulario = ReservaForm(request.POST, instance=reserva)

            if formulario.is_valid():
                formulario.save()
                return HttpResponse("<h1>Reserva modificada con exito</h1>")

        else:
            formulario = ReservaForm(instance=reserva)

        context = {'formulario': formulario}

        return render(request, 'modificar_reserva.html', context)

    except ObjectDoesNotExist as e:
        return HttpResponse("<h1>Reserva inexistente</h1>")


def eliminar_reserva(request, id):
    try:
        reserva = Reserva.objects.get(id=id)
        reserva.delete()
        return HttpResponse("<h1>Reserva eliminada con exito</h1>")
    except ObjectDoesNotExist as e:
        return HttpResponse("<h1>Reserva inexistente</h1>")
