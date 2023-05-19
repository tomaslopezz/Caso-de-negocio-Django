from django.contrib import admin
from .models import Empleado


# Register your models here.
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'nro_legajo', 'activo')
    search_fields = ('nombre', 'apellido')
    list_filter = ('activo',)


admin.register(Empleado, EmpleadoAdmin)
