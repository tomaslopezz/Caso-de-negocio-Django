from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Empleado, empleado_modificado, empleado_inexistente
from .forms import EmpleadoForm


# Create your views here.
def agregar_empleado(request):
    formulario = EmpleadoForm()
    if request.method == 'POST':
        formulario = EmpleadoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            contexto = empleado_modificado('agregado')
            return render(request, 'avisos.html', contexto)
        else:
            return HttpResponseRedirect('/empleados/agregar')
    contexto = {'formulario': formulario}
    return render(request, 'agregar_empleado.html', contexto)


def listar_empleados(request):
    empleados = Empleado.objects.all()
    contexto = {'empleados': empleados}

    return render(request, 'listar_empleados.html', contexto)


def activar_empleado(request, id):
    contexto = dict()
    try:
        empleado = Empleado.objects.get(id=id)
        empleado.activo = True
        empleado.save()

        contexto = empleado_modificado('activado')

    except ObjectDoesNotExist:
        contexto = empleado_inexistente(id)

    finally:
        return render(request, 'avisos.html', contexto)


def desactivar_empleado(request, id):
    contexto = dict()
    try:
        empleado = Empleado.objects.get(id=id)
        empleado.activo = False
        empleado.save()

        contexto = empleado_modificado('desactivado')

    except ObjectDoesNotExist:
        contexto = empleado_inexistente(id)

    finally:
        return render(request, 'avisos.html', contexto)


def modificar_empleado(request, id):
    try:
        empleado = Empleado.objects.get(id=id)

        if request.method == 'POST':
            formulario = EmpleadoForm(request.POST, instance=empleado)

            if formulario.is_valid():
                formulario.save()
                contexto = empleado_modificado('modificado')
                return render(request, 'avisos.html', contexto)

        else:
            formulario = EmpleadoForm(instance=empleado)

        contexto = {'formulario': formulario}

        return render(request, 'modificar_empleado.html', contexto)

    except ObjectDoesNotExist:
        contexto = empleado_inexistente(id)
        return render(request, 'avisos.html', contexto)
