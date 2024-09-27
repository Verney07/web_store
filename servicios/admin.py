from django.contrib import admin

from .models import Servicio

# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    """
    A class to show the 'created' and 'updated' fields
    in the admin site.
    """
    readonly_fields=('created', 'updated')

admin.site.register(Servicio, ServicioAdmin)
