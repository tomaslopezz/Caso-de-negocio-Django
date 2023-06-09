from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from servicios.models import Servicio
from clientes.models import Cliente
from coordinadores.models import Coordinador
from empleados.models import Empleado


# Create your views here.
def listar_servicios(request):
    """
    Vista que devuelve un listado de servicios en formato JSON.

    Recupera todos los objetos Servicio de la base de datos y crea una lista vacía llamada 'data' para almacenar
    los registros de servicios.
    Itera sobre cada uno de los objetos Servicio obtenido, crea un diccionario llamado 'registro' con
    las siguientes claves:
        - 'id': El ID del servicio.
        - 'nombre': El nombre del servicio.
        - 'precio': El precio del servicio.
    Luego agrega el 'registro' a la lista 'data'

    Parámetro request: Objeto HttpRequest que contiene los datos de la solicitud.
    return: JsonResponse que contiene el listado de servicios en formato JSON.
    """
    servicios = Servicio.objects.all()
    data = list()

    for servicio in servicios:
        registro = {'id': servicio.id,
                    'nombre': servicio.nombre,
                    'precio': servicio.precio}
        data.append(registro)

    return JsonResponse(data, safe=False)


def obtener_servicio(request, id):
    """
    Vista que obtiene los detalles de un servicio específico y devuelve un objeto JsonResponse.

    Recibe el ID del servicio como parámetro y busca un objeto Servicio correspondiente en la base de datos.
    Si encuentra el servicio, crea un diccionario 'data' con la clave 'servicio' que contiene una lista.
    Dentro de esa lista se agrega un diccionario que contiene los detalles del servicio con las siguientes claves:
        - 'id': El ID del servicio.
        - 'nombre': El nombre del servicio.
        - 'descripcion': 'La descripción del servicio'
        - 'precio': El precio del servicio.
    Si no encuentra el servicio, la lista 'servicio' será vacía.

    Parámetro request: Objeto HttpRequest que contiene los datos de la solicitud.
    Parámetro id: ID del servicio a obtener.
    return: JsonResponse que contiene los datos del servicio especificado dentro de una lista en  la clave 'servicio'
    del diccionario 'data'.
    """
    data = dict()
    try:
        servicio = Servicio.objects.get(id=id)

        data['servicio'] = [
                            {'id': servicio.id,
                             'nombre': servicio.nombre,
                             'descripcion': servicio.descripcion,
                             'precio': servicio.precio}
                            ]

    except ObjectDoesNotExist as e:
        data['servicio'] = []

    finally:
        return JsonResponse(data)
  
  
def listar_clientes(request):
    """
    Vista que devuelve un listado de clientes en formato JSON.

    Recupera todos los objetos Cliente de la base de datos y crea una lista vacía llamada 'data' para almacenar
    los registros de clientes.
    Itera sobre cada uno de los objetos Cliente obtenido, crea un diccionario llamado 'registro' con
    las siguientes claves:
        - 'id': El ID del cliente.
        - 'nombre': El nombre del cliente.
        - 'apellido': El apellido del cliente.
        - 'activo': Indicativo de sí el cliente está activo o no.
    Luego agrega el 'registro' a la lista 'data'

    Parámetro request: Objeto HttpRequest que contiene los datos de la solicitud.
    return: JsonResponse que contiene el listado de clientes en formato JSON.
    """
    clientes = Cliente.objects.all()
    data = list()

    for cliente in clientes:
        registro = {
            'id': cliente.id,
            'nombre': cliente.nombre,
            'apellido': cliente.apellido,
            'activo': cliente.activo
        }
        data.append(registro)
    
    return JsonResponse(data,safe=False)  


def listar_coordinadores(request):
    """
    Vista que devuelve un listado de coordinadores en formato JSON.

    Recupera todos los objetos Coordinador de la base de datos y crea una lista vacía llamada 'data' para almacenar
    los registros de coordinadores.
    Itera sobre cada uno de los objetos Coordinador obtenido, crea un diccionario llamado 'registro' con
    las siguientes claves:
        - 'id': El ID del coordinador.
        - 'nombre': El nombre del coordinador.
        - 'apellido': El apellido del coordinador.
        - 'dni': El DNI del coordinador.
        - 'fecha_alta': La fecha en la que fue dado de alta el coordinador.
        - 'activo': Indicativo de sí el coordinador está activo o no.
    Luego agrega el 'registro' a la lista 'data'

    Parámetro request: Objeto HttpRequest que contiene los datos de la solicitud.
    return: JsonResponse que contiene el listado de coordinadores en formato JSON.
    """
    coordinadores = Coordinador.objects.all()
    data = list()

    for coordinador in coordinadores:
        registro = {'id': coordinador.id,
                    'nombre': coordinador.nombre,
                    'apellido': coordinador.apellido,
                    'dni': coordinador.dni,
                    'fecha_alta': coordinador.fecha_alta,
                    'activo': coordinador.activo}
        data.append(registro)

    return JsonResponse(data, safe=False)


def listar_empleados(request):
    """
    Vista que devuelve un listado de empleados en formato JSON.

    Recupera todos los objetos Empleado de la base de datos y crea una lista vacía llamada 'data' para almacenar
    los registros de empleados.
    Itera sobre cada uno de los objetos Empleado obtenido, crea un diccionario llamado 'registro' con
    las siguientes claves:
        - 'id': El ID del empleado.
        - 'nombre': El nombre del empleado.
        - 'apellido': El apellido del empleado.
        - 'nro_legajo': El número de legajo del empleado.
        - 'activo': Indicativo de sí el empleado está activo o no.
    Luego agrega el 'registro' a la lista 'data'

    Parámetro request: Objeto HttpRequest que contiene los datos de la solicitud.
    return: JsonResponse que contiene el listado de empleados en formato JSON.
    """
    empleados = Empleado.objects.all()
    data = list()

    for empleado in empleados:
        registro = {'id': empleado.id,
                    'nombre': empleado.nombre,
                    'apellido': empleado.apellido,
                    'nro_legajo': empleado.nro_legajo,
                    'activo': empleado.activo}
        data.append(registro)

    return JsonResponse(data, safe=False)
