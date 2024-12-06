from django.shortcuts import render

# Create your views here.
def autenticacion(request):
    """Users can sing in."""
    return render(request, "autenticacion/registro.html")
