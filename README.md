# Eventos Salta
Aplicación Web desarollada para Bootcamp Django - Alkemy. Caso de negocio N°1 - App de Eventos

- Comisión: 5
- Squad: 1
- Mentor: Alejandro Palacios


## Conocimientos aplicados

- Python/Django
- POO
- Base de datos
## Tecnologias usadas

**Frameworks:** ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

**Base de datos:** ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

**Templates:** ![Jinja](https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black)

[Ir a la sección de Instalación](#instalacion)

[Documentacion](#documentacion)

## Autores
- [Matías Gómez](https://github.com/Mati2173)
- [Tomas Lopez](https://github.com/tomaslopezz)
- [Ariel Herrera](https://github.com/arielfherrera)

## Endpoints

[Clientes](#endpoints-de-clientes) |   [Coordinadores](#endpoints-de-coordinadores) |  [Empleados](#endpoints-de-empleados)   |   [Reservas](#endpoints-de-reservas) |  [Servicios](#endpoins-de-servicios)

## Funcionalidades (Features)

- Clientes
  - [x] Registro
  - [x] Listado
  - [x] Actualización
  - [x] Activación/Desactivación
- Coordinadores
  - [x] Registro
  - [x] Listado
  - [x] Actualización
  - [x] Activación/Desactivación
- Empleados
  - [x] Registro
  - [x] Listado
  - [x] Actualización
  - [x] Activación/Desactivación
- Reservas
  - [x] Registro
  - [x] Listado
  - [x] Actualización
  - [x] Eliminación
- Servicios
  - [x] Registro
  - [x] Listado
  - [x] Actualización
  - [x] Activación/Desactivación

## Requisitos previos

- Python 3.9 o superior
- Django 4.0
- Jinja2

## Instalacion

1. Clona este repositorio en tu máquina local:

2. Ve al directorio del proyecto:

3. Crea un entorno virtual para el proyecto:

4. Activa el entorno virtual:

- En macOS y Linux:

  ```
  source nombre-env/bin/activate
  ```

- En Windows:

    ```
    nombre-env\Scripts\activate
    ```

5. Instala las dependencias del proyecto:

    ```
    pip install -r requirements.txt
    ```

6. Ejecuta las migraciones:

    ```
    python manage.py migrate
    ```

7. Crea un superusuario:

    ```
    python manage.py createsuperuser
    ```

8. Ejecuta el servidor de desarrollo:

    ```
    python manage.py runserver
    ```

9. Visita [http://localhost:8000/](http://localhost:8000) en tu navegador.

## Documentacion

## Endpoints

# *Clientes*

### Endpoints de Clientes

| Método | Endpoint | Descripción |
| ------ | -------- | ----------- |
| GET    | [/clientes/listar/](#)| Listado de clientes |
| POST   | [/clientes/agregar/](#) | Crear un cliente |
| GET    | [/api/clientes/](#) | Obtener la lista de clientes |
| GET | [/clientes/activar/{id}](#) | Activa un cliente
| PUT    | [/clientes/modificar/{id}/modificar](#) | Actualizar un cliente |
| GET | [/clientes/desactivar/{id}](#) | Desactiva un cliente |

# *Coordinadores*

### Endpoints de coordinadores

| Método | Endpoint | Descripción |
| ------ | -------- | ----------- |
| GET    | [/coordinadores/listar/](#)| Listado de coordinadores |
| POST   | [/coordinadores/agregar/](#) | Crear un coordinador |
| GET    | [/api/coordinadores/](#) | Obtener la lista de coordinadores |
| PUT    | [/coordinadores/modificar/{id}/modificar](#) | Actualizar un coordinador |
| GET | [/coordinadores/activar/{id}](#) | Activa un coordinador
| GET | [/coordinadores/desactivar/{id}](#) | Desactiva un coordinador |

# *Empleados*

### Endpoints de Empleados

| Método | Endpoint | Descripción |
| ------ | -------- | ----------- |
| GET    | [/empleados/listar/](#)| Listado de empleados |
| POST   | [/empleados/agregar/](#) | Crear un empleado |
| GET    | [/api/empleados/](#) | Obtener la lista de empleados |
| GET | [/empleados/activar/{id}](#) | Activa un empleado
| PUT    | [/empleados/modificar/{id}/modificar](#) | Actualizar un empleado |
| GET | [/empleados/desactivar/{id}](#) | Desactiva un empleado |

# *Reservas*

### Endpoints de rerservas

| Método | Endpoint | Descripción |
| ------ | -------- | ----------- |
| GET    | [/reservas/listar/](#)| Listado de reservas |
| POST   | [/reservas/agregar/](#) | Crear una reserva |
| GET    | [/api/reservas/](#) | Obtener la lista de reservas |
| PUT    | [/reservas/modificar/{id}/modificar](#) | Actualizar una reserva |
| GET | [/reservas/eliminar/{id}](#) | Elimina una reserva |

# Servicios

### Endpoints de servicios

| Método | Endpoint | Descripción |
| ------ | -------- | ----------- |
| GET    | [/servicios/listar/](#)| Listado de servicios |
| POST   | [/servicios/agregar/](#) | Crear un servicio |
| GET    | [/api/servicios/](#) | Obtener la lista de servicios |
| PUT    | [/servicios/modificar/{id}/modificar](#) | Actualizar un servicio |
| GET | [/servicios/activar/{id}](#) | Activa un servicio
| GET | [/servicios/desactivar/{id}](#) | Desactiva un servicio

Para documentación detallada sobre las funcionalidades de cada aplicación consultar los archivos [views.py](#) de las distintas apps del proyecto.
