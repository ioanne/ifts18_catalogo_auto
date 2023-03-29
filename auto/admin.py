from django.contrib import admin

from auto.models import Auto

@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    
    list_display = (
        'marca',
        'modelo',
    )
