from django.urls import path
from . import views

urlpatterns = [
    path('agregar/', views.agregar_reserva, name='agregar-reserva'),
    path('eliminar/<int:id>', views.eliminar_reserva, name='eliminar-reserva')
]