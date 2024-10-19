from django.db import models

# Create your models here.

class Servicio(models.Model):
    "Model that define the option of Servicios"
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='servicios')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Definition of verbose_name and verbose_name_plural."""
        verbose_name = 'servicio'
        verbose_name_plural = 'servicio'
    
    def __str__(self): 
        return self.titulo