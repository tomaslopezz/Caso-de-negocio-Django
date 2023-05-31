from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from .forms import ReservaForm

# Create your views here.
def agregar_reserva(request):
    formulario = ReservaForm()
    if request.method == 'POST':
        formulario = ReservaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            return HttpResponseRedirect('/agregar_reserva/')
    contexto = {
        'formulario': formulario
    }
    return render(request, 'agregar_reserva.html', context=contexto)


def modificar_reserva(request, id):
    try:
        reserva = get_object_or_404(Reserva, id=id)

        if request.method == 'POST':
            formulario = ReservaForm(request.POST, instance=reserva)

            if formulario.is_valid():
                formulario.save()
                return HttpResponse("<h1>Reserva modificada con exito</h1>")

        else:
            formulario = ReservaForm(instance=reserva)

        context = {'formulario': formulario}

        return render(request, 'modificar_reserva.html', context)

    except Http404 as e:
        return HttpResponse("<h1>Reserva inexistente</h1>")