from django.shortcuts import render, HttpResponse

from carro.carro import Carro

# Create your views here.

def home(request):
    """Creates the 'Home' page"""

    carro=Carro(request)

    return render(request, "Proyecto_Web_App/home.html")
