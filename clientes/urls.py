from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar_clientes, name='listar-clientes'),
    path('modificar/<int:id>', views.modificar_cliente, name='modificar-cliente'),
    path('agregar/', views.agregar_cliente, name='agregar-cliente'),
    path('activar/<int:id>', views.activar_cliente, name='activar-cliente')
]

