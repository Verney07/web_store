"Models added to 'Administration Panel'"
from django.contrib import admin
from .models import CategoriaProd, Producto
# Register your models here.

class CategoriaProdAdmin(admin.ModelAdmin):
    """A class that define only read fields for 'Categoriaprod' view."""
    readonly_fields=("created","updated")

class ProductoProdAdmin(admin.ModelAdmin):
    """A class that define only read fields for 'Producto' view."""
    readonly_fields=("created","updated")

admin.site.register(CategoriaProd, CategoriaProdAdmin)
admin.site.register(Producto, ProductoProdAdmin)
