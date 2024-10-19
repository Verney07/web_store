from django.contrib import admin

from .models import Categoria, Post
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    "A class that allow addition categories from Admin site."
    readonly_fields=('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    "A class that allow addition posts from Admin site."
    readonly_fields=('created', 'updated')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)
