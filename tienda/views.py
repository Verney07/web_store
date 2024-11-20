"""The views for the 'tienda' app."""
from django.shortcuts import render

# Create your views here.

def tienda(request):
    """A view that render 'tienda' web page."""
    return render(request, "tienda/tienda.html")
