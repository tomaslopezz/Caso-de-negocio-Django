from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar_reservas, name='listar-reservas'),
    path('agregar/', views.agregar_reserva, name='agregar-reserva'),
    path('eliminar/<int:id>', views.eliminar_reserva, name='eliminar-reserva'),
    path('modificar/<int:id>', views.modificar_reserva, name='modificar-reserva')
]