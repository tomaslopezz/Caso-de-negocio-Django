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
  
  
def listar_coordinadores(request):
    coordinadores = Coordinador.objects.all()
    context = {'coordinadores':coordinadores}

    return render(request,'listado', context)


def registrar_coordinador(request):
    formulario = CoordinadorForm()
    if request.method == 'POST':
        formulario = CoordinadorForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            return HttpResponse('/registrar_coordinador/')
    context = {'formulario':formulario}

    return render(request, 'registrar_coordinador.html', context)


def desactivar_coordinador(request, id):
    coordinador = Coordinador.objects.get(id=id)
    coordinador.activo = False
    coordinador.save()
    return HttpResponse("<h1>Coordinador desactivado con exito</h1>")



