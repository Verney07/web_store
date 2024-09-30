from django.shortcuts import render

from servicios.models import Servicio

# Create your views here.

def servicios(request):
    "A view that shows all app services"
    servicios = Servicio.objects.all()

    return render(request, "servicios/servicios.html", {"servicios": servicios})