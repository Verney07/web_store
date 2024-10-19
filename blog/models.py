from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    "Model that define the Category's options"
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
    
    def __str__(self): 
        return self.nombre


class Post(models.Model):
    "Model that define the Post's options"
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='blog', null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categorias=models.ManyToManyField(Categoria)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Definition of verbose_name and verbose_name_plural."""
        verbose_name = 'post'
        verbose_name_plural = 'posts'
    
    def __str__(self): 
        return self.titulo