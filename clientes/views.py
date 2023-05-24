from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Cliente
from .forms  import ClienteForm 

# Create your views here.
def activar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.activo = True
    cliente.save()
    return HttpResponse("<h1>Cliente activado con exito</h1>")

def actualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'POST':
        formulario = ClienteForm(request.POST, instance=cliente)

        if formulario.is_valid():
            formulario.save()
            return HttpResponse("<h1>Cliente modificado con exito</h1>")
        
        else:
            formulario = ClienteForm(instance=cliente)
        
        context = {'formulario':formulario}

        return render(request, 'modificar_cliente.jinja', context)

