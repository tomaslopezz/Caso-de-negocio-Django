from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import HttpResponseRedirect, Http404
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

def modificar_servicio(request, id):
    try:
        servicio = get_object_or_404(Servicio, id=id)

        if request.method == 'POST':
            formulario = ServicioForm(request.POST, instance=servicio)

            if formulario.is_valid():
                formulario.save()
                return HttpResponse("<h1>Servicio modificado con exito</h1>")

        else:
            formulario = ServicioForm(instance=servicio)

        context = {'formulario': formulario}

        return render(request, 'modificar_servicio.html', context)

    except Http404 as e:
        return HttpResponse("<h1>Servicio inexistente</h1>")