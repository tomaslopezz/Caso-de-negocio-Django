from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReservaForm
from .models import Reserva, reserva_modificada, reserva_inexistente


# Create your views here.
def agregar_reserva(request):
    if request.method == 'POST':
        formulario = ReservaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            contexto = reserva_modificada('agregada')
            return render(request, 'avisos.html', contexto)
        else:
            return HttpResponseRedirect('/reservas/agregar')
    else:
        formulario = ReservaForm()

    contexto = {'formulario': formulario}

    return render(request, 'agregar_reserva.html', contexto)


def listar_reservas(request):
    reservas = Reserva.objects.all()
    contexto = {'reservas': reservas}
    return render(request, 'listar_reservas.html', contexto)


def modificar_reserva(request, id):
    try:
        reserva = Reserva.objects.get(id=id)

        if request.method == 'POST':
            formulario = ReservaForm(request.POST, instance=reserva)

            if formulario.is_valid():
                formulario.save()
                contexto = reserva_modificada('modificada')
                return render(request, 'avisos.html', contexto)

        else:
            formulario = ReservaForm(instance=reserva)

        contexto = {'formulario': formulario}

        return render(request, 'modificar_reserva.html', contexto)

    except ObjectDoesNotExist:
        contexto = reserva_inexistente(id)
        return render(request, 'avisos.html', contexto)


def eliminar_reserva(request, id):
    contexto = dict()
    try:
        reserva = Reserva.objects.get(id=id)
        reserva.delete()

        contexto = reserva_modificada('eliminada')

    except ObjectDoesNotExist:
        contexto = reserva_inexistente(id)

    finally:
        return render(request, 'avisos.html', contexto)
