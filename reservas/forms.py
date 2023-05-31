from django import forms
from .models import Reserva


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ('fecha_reserva', 'fecha_servicio', 'cliente',
                   'servicio', 'empleado', 'coordinador')
        labels = {'Fecha Reserva', 'Fecha Servicio', 'Cliente',
                   'Servicio', 'Empleado', 'Coordinador',
                  }
