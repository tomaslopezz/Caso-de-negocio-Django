from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar_empleados, name='listar-empleados'),
    path('agregar/', views.agregar_empleado, name='agregar-empleado'),
    path('activar/<int:id>', views.activar_empleado, name='activar-empleado'),
    path('desactivar/<int:id>', views.desactivar_empleado, name='desactivar-empleado'),
    path('modificar/<int:id>', views.actualizar_empleado, name='modificar-empleado')
]