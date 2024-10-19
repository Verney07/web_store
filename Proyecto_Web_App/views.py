from django.shortcuts import render, HttpResponse

from servicios.models import Servicio

# Create your views here.

def home(request):

    return render(request, "Proyecto_Web_App/home.html")


def tienda(request):

    return render(request, "Proyecto_Web_App/tienda.html")


def contacto(request):

    return render(request, "Proyecto_Web_App/contacto.html")
