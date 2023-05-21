from django import forms
from .models import Empleado


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ('nombre', 'apellido', 'nro_legajo')
        labels = {'nombre': 'Nombre',
                  'apellido': 'Apellido',
                  'nro_legajo': 'N° Legajo',
                  }
