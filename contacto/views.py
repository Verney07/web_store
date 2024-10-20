from django.shortcuts import render

from .forms import FormularioContacto

# Create your views here.

def contacto(request):
    """A view that render 'contacto' web page."""
    formulario_contacto=FormularioContacto()
    return render(request, "contacto/contacto.html", {'miFormulario': formulario_contacto})


