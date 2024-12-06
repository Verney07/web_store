"""Views of the app 'tienda'"""
from django.shortcuts import redirect
from tienda.models import Producto
from .carro import Carro

# Create your views here.

def agregar_producto(request, producto_id):
    """View to add a new products to shopping cart."""
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    """View to delete products to shopping cart."""
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    """View to subtract products to shopping cart."""
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.restar(producto=producto)
    return redirect("Tienda")

def vaciar_productos(request):
    """View to empty the shopping cart."""
    carro=Carro(request)
    carro.vaciar_carro()
    return redirect("Tienda")
