from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Empleado, empleado_modificado, empleado_inexistente
from .forms import EmpleadoForm


def agregar_empleado(request):
    """
    Vista para agregar un empleado.

    Permite al usuario agregar un empleado utilizando el formulario EmpleadoForm.

    Método HTTP admitidos: GET, POST.

    Si el método es POST y el formulario es válido, el empleado se guarda en la base de datos.
    Si el método es POST y el formulario no es válido, se redirige a la página de agregar empleado para corregir los errores.
    
    parametro request: Objeto HttpRequest que contiene los datos de la solicitud.
    return: HttpResponse con la representación de la plantilla 'agregar_empleado.html' que muestra un formulario para agrgar un empleado.
    """
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
    """
    Vista para listar todos los empleados.

    Recupera todos los objetos Empleado de la base de datos y los pasa como contexto a la plantilla 'listar_empleados.html'.

    parametro request: Objeto HttpRequest que contiene los datos de la solicitud.
    return: HttpResponse con la representación de la plantilla 'listar_empleados.html' que muestra la lista de empleados.
    """
    empleados = Empleado.objects.all()
    contexto = {'empleados': empleados}

    return render(request, 'listar_empleados.html', contexto)


def activar_empleado(request, id):
    """
    Vista para activar un empleado.

    Recibe el ID del empleado como parámetro y busca un objeto Empleado correspondiente en la base de datos.
    Si encuentra el empleado, establece su atributo 'activo' como True y guarda los cambios en la base de datos.
    Retorna una HttpResponse con un mensaje de éxito si el empleado se activó correctamente.
    Retorna una HttpResponse con un mensaje de error si el empleado no existe.

    parametro request: Objeto HttpRequest que contiene los datos de la solicitud.
    parametro id: ID del empleado a activar.
    return: HttpResponse con un mensaje de éxito o error y la opcion de regresar al listado.
    """
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
    """
    Vista para desactivar un empleado.

    Recibe el ID del empleado como parámetro y busca un objeto Empleado correspondiente en la base de datos.
    Si encuentra el empleado, establece su atributo 'activo' como False y guarda los cambios en la base de datos.
    Retorna una HttpResponse con un mensaje de éxito si el empleado se desactivó correctamente.
    Retorna una HttpResponse con un mensaje de error si el empleado no existe.

    parametro request: Objeto HttpRequest que contiene los datos de la solicitud.
    parametro id: ID del empleado a desactivar.
    return: HttpResponse con un mensaje de éxito o error y la opcion de regresar al listado.
    """
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
    """
    Vista para modificar un empleado.

    Recibe el ID del empleado como parámetro y busca un objeto Empleado correspondiente en la base de datos.
    Si encuentra el empleado, se crea una instancia de EmpleadoForm con los datos del empleado.
    Si el método de la solicitud es POST, se valida el formulario y se guarda la modificación en la base de datos.
    Retorna una HttpResponse con un mensaje de éxito si el empleado se modificó correctamente.
    Si el método de la solicitud es GET, se muestra el formulario con los datos actuales del empleado.
    Retorna una HttpResponse con un mensaje de error si el empleado no existe.

    parametro request: Objeto HttpRequest que contiene los datos de la solicitud.
    parametro id: ID del empleado a modificar.
    return: HttpResponse con un mensaje de éxito o error, o una representación de la plantilla 'modificar_empleado.html' con el formulario y el contexto.
    """
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
