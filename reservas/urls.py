from django.urls import path
from . import views

urlpatterns = [
    path('eliminar/<int:id>', views.eliminar_reserva, name='eliminar-reserva')
]