"""The views for the 'tienda' app."""
from django.shortcuts import render
from .models import Producto
# Create your views here.

def tienda(request):
    """A view that render 'tienda' web page."""
    productos=Producto.objects.all()
    return render(request, "tienda/tienda.html", {"productos":productos})
