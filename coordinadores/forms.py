from django import forms
from .models import Coordinador


class CoordinadorForm(forms.ModelForm):

    class Meta:
        model = Coordinador
        fields = {'nombre', 'apellido', 'dni', 'fecha_alta'}
        labels = {'nombre': 'Nombre',
                  'apellido': 'Apellido',
                  'dni': 'DNI',
                  'fecha_alta': 'Fecha de alta'
                  }
