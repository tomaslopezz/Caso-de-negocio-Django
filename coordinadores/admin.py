from django.contrib import admin
from .models import Coordinador


# Register your models here.
class CoordinadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'fecha_alta', 'activo')
    search_fields = ('nombre', "apellido")
    list_filter = ('activo',)


admin.site.register(Coordinador, CoordinadorAdmin)