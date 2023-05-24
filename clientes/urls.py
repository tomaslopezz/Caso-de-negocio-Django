from django.urls import path
from . import views

urlpatterns = [
    path('agregar/', views.agregar_cliente, name='agregar-empleado'),
    path('activar/<int:id>', views.activar_cliente)
]
