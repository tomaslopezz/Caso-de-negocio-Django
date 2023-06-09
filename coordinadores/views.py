from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Coordinador, coordinador_modificado, coordinador_inexistente
from .forms import CoordinadorForm


# Create your views here.
def modificar_coordinador(request, id):
    """
    Vista para modificar un coordinador.

    Recibe el ID del coordinador como parámetro y busca un objeto Coordinador correspondiente en la base de datos.
    Si encuentra el coordinador, se crea una instancia de CoordinadorForm con los datos del coordinador.
    Si el método de la solicitud es POST, se valida el formulario y se guarda la modificación en la base de datos.
    Retorna una HttpResponse con un mensaje de éxito si el coordinador se modificó correctamente.
    Si el método de la solicitud es GET, se muestra el formulario con los datos actuales del coordinador.
    Retorna una HttpResponse con un mensaje de error si el coordinador no existe.

    Parámetro request: Objeto HttpRequest que contiene los datos de la solicitud.
    Parámetro id: ID del coordinador a modificar.
    return: HttpResponse con un mensaje de éxito o error, o una representación de la
    plantilla 'modificar_coordinador.html' con el formulario y el contexto.
    """
    try:
        coordinador = Coordinador.objects.get(id=id)

        if request.method == 'POST':
            formulario = CoordinadorForm(request.POST, instance=coordinador)

            if formulario.is_valid():
                formulario.save()
                contexto = coordinador_modificado('modificado')
                return render(request, 'avisos.html', contexto)

        else:
            formulario = CoordinadorForm(instance=coordinador)

        contexto = {'formulario': formulario}

        return render(request, 'modificar_coordinador.html', contexto)

    except ObjectDoesNotExist:
        contexto = coordinador_inexistente(id)
        return render(request, 'avisos.html', contexto)
  
  
def listar_coordinadores(request):
    """
    Vista para listar todos los coordinadors.

    Recupera todos los objetos Coordinador de la base de datos y los pasa como contexto a la
    plantilla 'listar_coordinadors.html'.

    Parámetro request: Objeto HttpRequest que contiene los datos de la solicitud.
    return: HttpResponse con la representación de la plantilla 'listar_coordinadores.html' que muestra
    la lista de coordinadores
    """
    coordinadores = Coordinador.objects.all()
    contexto = {'coordinadores': coordinadores}

    return render(request, 'listar_coordinadores.html', contexto)


def agregar_coordinador(request):
    """
    Vista para agregar un coordinador.

    Permite al usuario agregar un coordinador utilizando el formulario CoordinadorForm.

    Método HTTP admitidos: GET, POST.

    Si el método es POST y el formulario es válido, el coordinador se guarda en la base de datos y se redirige a la
    página de avisos.
    Si el método es POST y el formulario no es válido, se redirige a la página de agregar coordinador para corregir
    los errores.

    Parámetro request: Objeto HttpRequest que contiene los datos de la solicitud.
    return: HttpResponse con la representación de la plantilla 'agregar_coordinador.html' que muestra un formulario para
    agregar un coordinador.
    """
    formulario = CoordinadorForm()
    if request.method == 'POST':
        formulario = CoordinadorForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            contexto = coordinador_modificado('agregado')
            return render(request, 'avisos.html', contexto)
        else:
            return HttpResponseRedirect('/coordinadores/agregar')
    contexto = {'formulario': formulario}

    return render(request, 'agregar_coordinador.html', contexto)


def activar_coordinador(request, id):
    """
    Vista para activar un coordinador.

    Recibe el ID del coordinador como parámetro y busca un objeto Coordinador correspondiente en la base de datos.
    Si encuentra el coordinador, establece su atributo 'activo' como True y guarda los cambios en la base de datos.
    Retorna una HttpResponse con un mensaje de éxito si el coordinador se activó correctamente.
    Retorna una HttpResponse con un mensaje de error si el coordinador no existe.

    Parámetro request: Objeto HttpRequest que contiene los datos de la solicitud.
    Parámetro id: ID del coordinador a activar.
    return: HttpResponse con un mensaje de éxito o error y la opción de regresar al listado.
    """
    contexto = dict()
    try:
        coordinador = Coordinador.objects.get(id=id)
        coordinador.activo = True
        coordinador.save()

        contexto = coordinador_modificado('activado')

    except ObjectDoesNotExist:
        contexto = coordinador_inexistente(id)

    finally:
        return render(request, 'avisos.html', contexto)


def desactivar_coordinador(request, id):
    """
    Vista para desactivar un coordinador.

    Recibe el ID del coordinador como parámetro y busca un objeto Coordinador correspondiente en la base de datos.
    Si encuentra el coordinador, establece su atributo 'activo' como False y guarda los cambios en la base de datos.
    Retorna una HttpResponse con un mensaje de éxito si el coordinador se desactivó correctamente.
    Retorna una HttpResponse con un mensaje de error si el coordinador no existe.

    Parámetro request: Objeto HttpRequest que contiene los datos de la solicitud.
    Parámetro id: ID del coordinador a desactivar.
    return: HttpResponse con un mensaje de éxito o error y la opción de regresar al listado.
    """
    contexto = dict()
    try:
        coordinador = Coordinador.objects.get(id=id)
        coordinador.activo = False
        coordinador.save()

        contexto = coordinador_modificado('desactivado')

    except ObjectDoesNotExist:
        contexto = coordinador_inexistente(id)

    finally:
        return render(request, 'avisos.html', contexto)
