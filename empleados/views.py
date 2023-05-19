from django.shortcuts import render
from .models import Empleado

# Create your views here.
def listar_empleados(request):
    empleados = Empleado.objects.all()
    context = {'empleados': empleados}

    return render(request, 'lista_empleados.jinja', context)



