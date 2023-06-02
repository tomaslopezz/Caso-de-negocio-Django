from django import forms
from .models import Reserva


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ('fecha_reserva', 'fecha_servicio', 'cliente',
                  'servicio', 'empleado', 'coordinador')
        labels = {'fecha_reserva': 'Fecha de la reserva',
                  'fecha_servicio': 'Fecha del servicio',
                  'cliente': 'Cliente',
                  'servicio': 'Servicio',
                  'empleado': 'Empleado',
                  'coordinador': 'Coordinador'}
