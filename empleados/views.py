from django.shortcuts import render, HttpResponse
from .models import Empleado

# Create your views here.
def listar_empleados(request):
    empleados = Empleado.objects.all()
    context = {'empleados': empleados}

    return render(request, 'lista_empleados.jinja', context)

def activar_empleado(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.activo = True
    empleado.save()
    return HttpResponse("<h1>Empleado activado con exito</h1>")