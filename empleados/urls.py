from django.urls import path
from . import views

urlpatterns = [
    path('activar_empleado/<int:id>', views.activar_empleado, name='activar-empleado'),
    path('desactivar_empleado/<int:id>', views.desactivar_empleado, name='desactivar-empleado'),
]