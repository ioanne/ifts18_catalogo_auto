from django.contrib import admin

from .models import Marca

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    """ Esto es un DOCstring """

    list_display = (
        'nombre',
        'descripcion',

    )
    list_filter = ('nombre', 'descripcion')
    search_fields = ('nombre', 'descripcion')
    list_per_page = 10
