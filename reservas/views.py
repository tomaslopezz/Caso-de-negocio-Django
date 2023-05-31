from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReservaForm

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
