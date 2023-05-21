from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from .models import Empleado
from .forms import EmpleadoFormulario

# Create your views here.

def agregar_empleado(request):
    formulario = EmpleadoFormulario()
    if request.method == 'POST':
        formulario = EmpleadoFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            return HttpResponseRedirect('/agregar_empleado/')
    contexto = {
        'formulario' : formulario
    }
    return render(request, 'agregar_empleado.jinja', context=contexto)

def listar_empleados(request):
    empleados = Empleado.objects.all()
    context = {'empleados': empleados}

    return render(request, 'lista_empleados.jinja', context)


def activar_empleado(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.activo = True
    empleado.save()
    return HttpResponse("<h1>Empleado activado con exito</h1>")

  
def desactivar_empleado(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.activo = False
    empleado.save()
    return HttpResponse("<h1>Empleado desactivado con exito</h1>")
