from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Servicio, servicio_modificado, servicio_inexistente
from .forms import ServicioForm


# Create your views here.
def agregar_servicio(request):
    """
    Vista para agregar un servicio.

    Permite al usuario agregar un servicio utilizando el formulario ServicioForm.

    Método HTTP admitidos: GET, POST.

    Si el método es POST y el formulario es válido, el servicio se guarda en la base de datos y se redirige a la
    página de avisos.
    Si el método es POST y el formulario no es válido, se redirige a la página de agregar servicio para corregir
    los errores.

    Parámetro request: Objeto HttpRequest que contiene los datos de la solicitud.
    return: HttpResponse con la representación de la plantilla 'agregar_servicio.html' que muestra un formulario para
    agregar un servicio
    """
    formulario = ServicioForm()
    if request.method == 'POST':
        formulario = ServicioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            contexto = servicio_modificado('agregado')
            return render(request, 'avisos.html', contexto)
        else:
            return HttpResponseRedirect('/servicios/agregar')
    contexto = {'formulario': formulario}
    return render(request, 'agregar_servicio.html', contexto)


def listar_servicios(request):
    """
    Vista para listar todos los servicios.

    Recupera todos los objetos Servicio de la base de datos y los pasa como contexto a la
    plantilla 'listar_servicios.html'.

    Parámetro request: Objeto HttpRequest que contiene los datos de la solicitud.
    return: HttpResponse con la representación de la plantilla 'listar_servicios.html' que muestra la lista de servicios
    """
    servicios = Servicio.objects.all()
    contexto = {'servicios': servicios}
    return render(request, 'listar_servicios.html', contexto)


def activar_servicio(request, id):
    """
    Vista para activar un servicio.

    Recibe el ID del servicio como parámetro y busca un objeto Servicio correspondiente en la base de datos.
    Si encuentra el servicio, establece su atributo 'activo' como True y guarda los cambios en la base de datos.
    Retorna una HttpResponse con un mensaje de éxito si el servicio se activó correctamente.
    Retorna una HttpResponse con un mensaje de error si el servicio no existe.

    Parámetro request: Objeto HttpRequest que contiene los datos de la solicitud.
    Parámetro id: ID del servicio a activar.
    return: HttpResponse con un mensaje de éxito o error y la opción de regresar al listado.
    """
    contexto = dict()
    try:
        servicio = Servicio.objects.get(id=id)
        servicio.activo = True
        servicio.save()

        contexto = servicio_modificado('activado')

    except ObjectDoesNotExist:
        contexto = servicio_inexistente(id)

    finally:
        return render(request, 'avisos.html', contexto)


def desactivar_servicio(request, id):
    """
    Vista para desactivar un servicio.

    Recibe el ID del servicio como parámetro y busca un objeto Servicio correspondiente en la base de datos.
    Si encuentra el servicio, establece su atributo 'activo' como False y guarda los cambios en la base de datos.
    Retorna una HttpResponse con un mensaje de éxito si el servicio se desactivó correctamente.
    Retorna una HttpResponse con un mensaje de error si el servicio no existe.

    Parámetro request: Objeto HttpRequest que contiene los datos de la solicitud.
    Parámetro id: ID del servicio a desactivar.
    return: HttpResponse con un mensaje de éxito o error y la opción de regresar al listado.
    """
    contexto = dict()
    try:
        servicio = Servicio.objects.get(id=id)
        servicio.activo = False
        servicio.save()

        contexto = servicio_modificado('desactivado')

    except ObjectDoesNotExist:
        contexto = servicio_inexistente(id)

    finally:
        return render(request, 'avisos.html', contexto)


def modificar_servicio(request, id):
    """
    Vista para modificar un servicio.

    Recibe el ID del servicio como parámetro y busca un objeto Servicio correspondiente en la base de datos.

    Si encuentra el servicio, se crea una instancia de ServicioForm con los datos del servicio.
    Si el método de la solicitud es POST, se valida el formulario y se guarda la modificación en la base de datos.
    Retorna una HttpResponse con un mensaje de éxito si el servicio se modificó correctamente.
    Si el método de la solicitud es GET, se muestra el formulario con los datos actuales del servicio.
    Retorna una HttpResponse con un mensaje de error si el servicio no existe.

    Parámetro request: Objeto HttpRequest que contiene los datos de la solicitud.
    Parámetro id: ID del servicio a modificar.
    return: HttpResponse con un mensaje de éxito o error, o una representación de la plantilla 'modificar_servicio.html'
    con el formulario y el contexto.
    """
    try:
        servicio = Servicio.objects.get(id=id)

        if request.method == 'POST':
            formulario = ServicioForm(request.POST, instance=servicio)

            if formulario.is_valid():
                formulario.save()
                contexto = servicio_modificado('modificado')
                return render(request, 'avisos.html', contexto)

        else:
            formulario = ServicioForm(instance=servicio)

        contexto = {'formulario': formulario}

        return render(request, 'modificar_servicio.html', contexto)

    except ObjectDoesNotExist:
        contexto = servicio_inexistente(id)
        return render(request, 'avisos.html', contexto)
