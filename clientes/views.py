from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Cliente, cliente_modificado, cliente_inexistente
from .forms import ClienteForm


# Create your views here.
def agregar_cliente(request):
    """
    Vista para agregar un cliente.

    Permite al usuario agregar un cliente utilizando el formulario ClienteForm.

    Método HTTP admitidos: GET, POST.

    Si el método es POST y el formulario es válido, el cliente se guarda en la base de datos y se redirige a la
    página de avisos.
    Si el método es POST y el formulario no es válido, se redirige a la página de agregar cliente para corregir
    los errores.

    Parámetro request: Objeto HttpRequest que contiene los datos de la solicitud.
    return: HttpResponse con la representación de la plantilla 'agregar_cliente.html' que muestra un formulario para
    agregar un cliente.
    """
    formulario = ClienteForm()
    if request.method == 'POST':
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            contexto = cliente_modificado('agregado')
            return render(request, 'avisos.html', contexto)
        else:
            return HttpResponseRedirect('/clientes/agregar')
    contexto = {'formulario': formulario}
    return render(request, 'agregar_cliente.html', contexto)


def listar_clientes(request):
    """
    Vista para listar todos los clientes.

    Recupera todos los objetos Cliente de la base de datos y los pasa como contexto a la
    plantilla 'listar_clientes.html'.

    Parámetro request: Objeto HttpRequest que contiene los datos de la solicitud.
    return: HttpResponse con la representación de la plantilla 'listar_clientes.html' que muestra la lista de clientes.
    """
    clientes = Cliente.objects.all()
    contexto = {'clientes': clientes}

    return render(request, 'listar_clientes.html', contexto)


def activar_cliente(request, id):
    """
    Vista para activar un cliente.

    Recibe el ID del cliente como parámetro y busca un objeto Cliente correspondiente en la base de datos.
    Si encuentra el cliente, establece su atributo 'activo' como True y guarda los cambios en la base de datos.
    Retorna una HttpResponse con un mensaje de éxito si el cliente se activó correctamente.
    Retorna una HttpResponse con un mensaje de error si el cliente no existe.

    Parámetro request: Objeto HttpRequest que contiene los datos de la solicitud.
    Parámetro id: ID del cliente a activar.
    return: HttpResponse con un mensaje de éxito o error y la opción de regresar al listado.
    """
    contexto = dict()
    try:
        cliente = Cliente.objects.get(id=id)
        cliente.activo = True
        cliente.save()

        contexto = cliente_modificado('activado')

    except ObjectDoesNotExist:
        contexto = cliente_inexistente(id)

    finally:
        return render(request, 'avisos.html', contexto)


def desactivar_cliente(request, id):
    """
    Vista para desactivar un cliente.

    Recibe el ID del cliente como parámetro y busca un objeto Cliente correspondiente en la base de datos.
    Si encuentra el cliente, establece su atributo 'activo' como False y guarda los cambios en la base de datos.
    Retorna una HttpResponse con un mensaje de éxito si el cliente se desactivó correctamente.
    Retorna una HttpResponse con un mensaje de error si el cliente no existe.

    Parámetro request: Objeto HttpRequest que contiene los datos de la solicitud.
    Parámetro id: ID del cliente a desactivar.
    return: HttpResponse con un mensaje de éxito o error y la opción de regresar al listado.
    """
    contexto = dict()
    try:
        cliente = Cliente.objects.get(id=id)
        cliente.activo = False
        cliente.save()

        contexto = cliente_modificado('desactivado')

    except ObjectDoesNotExist:
        contexto = cliente_inexistente(id)

    finally:
        return render(request, 'avisos.html', contexto)


def modificar_cliente(request, id):
    """
    Vista para modificar un cliente.

    Recibe el ID del cliente como parámetro y busca un objeto Cliente correspondiente en la base de datos.
    Si encuentra el cliente, se crea una instancia de ClienteForm con los datos del cliente.
    Si el método de la solicitud es POST, se valida el formulario y se guarda la modificación en la base de datos.
    Retorna una HttpResponse con un mensaje de éxito si el cliente se modificó correctamente.
    Si el método de la solicitud es GET, se muestra el formulario con los datos actuales del cliente.
    Retorna una HttpResponse con un mensaje de error si el cliente no existe.

    Parámetro request: Objeto HttpRequest que contiene los datos de la solicitud.
    Parámetro id: ID del cliente a modificar.
    return: HttpResponse con un mensaje de éxito o error, o una representación de la plantilla 'modificar_cliente.html'
    con el formulario y el contexto.
    """
    try:
        cliente = Cliente.objects.get(id=id)

        if request.method == 'POST':
            formulario = ClienteForm(request.POST, instance=cliente)

            if formulario.is_valid():
                formulario.save()
                contexto = cliente_modificado('modificado')
                return render(request, 'avisos.html', contexto)
        else:
            formulario = ClienteForm(instance=cliente)

        contexto = {'formulario': formulario}
        return render(request, 'modificar_cliente.html', contexto)

    except ObjectDoesNotExist:
        contexto = cliente_inexistente(id)
        return render(request, 'avisos.html', contexto)
