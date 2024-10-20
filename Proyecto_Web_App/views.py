from django.shortcuts import render, HttpResponse

from servicios.models import Servicio

# Create your views here.

def home(request):

    return render(request, "Proyecto_Web_App/home.html")


def tienda(request):
    """A view that render 'tienda' web page."""
    return render(request, "Proyecto_Web_App/tienda.html")
