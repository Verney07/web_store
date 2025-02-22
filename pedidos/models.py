from django.db import models

from django.db.models import F, Sum, FloatField
from django.contrib.auth import get_user_model
from tienda.models import Producto

# Create your models here.
User=get_user_model()

class Pedido(models.Model):
    """Creates the user's order."""
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
    
    @property
    def total(self):
        """Shows the total order amount."""
        return self.lineapedido_set.aggregate(

            total=Sum(F("precio")*F("cantidad"), output_field=FloatField())
        )["total"]

    class Meta:
        """Single and plural table name"""
        db_table='pedidos'
        verbose_name='pedido'
        verbose_name_plural='pedidos'
        ordering=['id']

class LineaPedido(models.Model):
    """Creates the products detail order."""
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido=models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.cantidad} unidades de {self.producto.nombre}'

    class Meta:
        """Single and plural table name"""
        db_table='lineapedidos'
        verbose_name='Linea Pedido'
        verbose_name_plural='Lineas Pedidos'
        ordering=['id']
            