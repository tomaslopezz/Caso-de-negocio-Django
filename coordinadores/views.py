from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Coordinador
from .forms import CoordinadorForm

# Create your views here.
def actualizar_coordinador(request, id):
    coordinador = get_object_or_404(Coordinador, id=id)

    if request.method == 'POST':
        formulario = CoordinadorForm(request.POST, instance=coordinador)

        if formulario.is_valid():
            formulario.save()
            return HttpResponse("<h1>Coordinador modificado con exito</h1>")

    else:
        formulario = CoordinadorForm(instance=coordinador)

    context = {'formulario': formulario}

    return render(request, 'modificar_coordinador.jinja', context)
