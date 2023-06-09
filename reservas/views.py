from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReservaForm
from .models import Reserva, reserva_modificada, reserva_inexistente


# Create your views here.
def agregar_reserva(request):
    """
    Vista para agregar un reserva.

    Permite al usuario agregar un reserva utilizando el formulario ReservaForm.

    Método HTTP admitidos: GET, POST.

    Si el método es POST y el formulario es válido, el reserva se guarda en la base de datos y se redirige a la
    página de avisos.
    Si el método es POST y el formulario no es válido, se redirige a la página de agregar reserva para corregir
    los errores.

    Parámetro request: Objeto HttpRequest que contiene los datos de la solicitud.
    return: HttpResponse con la representación de la plantilla 'agregar_reserva.html' que muestra un formulario para
    agregar un reserva.
    """
    if request.method == 'POST':
        formulario = ReservaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            contexto = reserva_modificada('agregada')
            return render(request, 'avisos.html', contexto)
        else:
            return HttpResponseRedirect('/reservas/agregar')
    else:
        formulario = ReservaForm()

    contexto = {'formulario': formulario}

    return render(request, 'agregar_reserva.html', contexto)


def listar_reservas(request):
    """
    Vista para listar todos los reservas.

    Recupera todos los objetos Reserva de la base de datos y los pasa como contexto a la
    plantilla 'listar_reservas.html'.

    Parámetro request: Objeto HttpRequest que contiene los datos de la solicitud.
    return: HttpResponse con la representación de la plantilla 'listar_reservas.html' que muestra la lista de reservas.
    """
    reservas = Reserva.objects.all()
    contexto = {'reservas': reservas}
    return render(request, 'listar_reservas.html', contexto)


def modificar_reserva(request, id):
    """
    Vista para modificar un reserva.

    Recibe el ID del reserva como parámetro y busca un objeto Reserva correspondiente en la base de datos.
    Si encuentra el reserva, se crea una instancia de ReservaForm con los datos del reserva.
    Si el método de la solicitud es POST, se valida el formulario y se guarda la modificación en la base de datos.
    Retorna una HttpResponse con un mensaje de éxito si el reserva se modificó correctamente.
    Si el método de la solicitud es GET, se muestra el formulario con los datos actuales del reserva.
    Retorna una HttpResponse con un mensaje de error si el reserva no existe.

    Parámetro request: Objeto HttpRequest que contiene los datos de la solicitud.
    Parámetro id: ID del reserva a modificar.
    return: HttpResponse con un mensaje de éxito o error, o una representación de la plantilla 'modificar_reserva.html'
    con el formulario y el contexto.
    """
    try:
        reserva = Reserva.objects.get(id=id)

        if request.method == 'POST':
            formulario = ReservaForm(request.POST, instance=reserva)

            if formulario.is_valid():
                formulario.save()
                contexto = reserva_modificada('modificada')
                return render(request, 'avisos.html', contexto)

        else:
            formulario = ReservaForm(instance=reserva)

        contexto = {'formulario': formulario}

        return render(request, 'modificar_reserva.html', contexto)

    except ObjectDoesNotExist:
        contexto = reserva_inexistente(id)
        return render(request, 'avisos.html', contexto)


def eliminar_reserva(request, id):
    """
    Vista para eliminar un reserva.

    Recibe el ID del reserva como parámetro y busca un objeto Reserva correspondiente en la base de datos.
    Si encuentra el reserva, la elimina y guarda los cambios en la base de datos.
    Retorna una HttpResponse con un mensaje de éxito si el reserva se eliminó correctamente.
    Retorna una HttpResponse con un mensaje de error si el reserva no existe.

    Parámetro request: Objeto HttpRequest que contiene los datos de la solicitud.
    Parámetro id: ID del reserva a eliminar.
    return: HttpResponse con un mensaje de éxito o error y la opción de regresar al listado.
    """
    contexto = dict()
    try:
        reserva = Reserva.objects.get(id=id)
        reserva.delete()

        contexto = reserva_modificada('eliminada')

    except ObjectDoesNotExist:
        contexto = reserva_inexistente(id)

    finally:
        return render(request, 'avisos.html', contexto)
