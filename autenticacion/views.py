"""The view functions of 'autentication' app."""
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
class VRegistro(View):
    """Manage the user-form"""

    def get(self, request):
        """Allows create a user-account."""
        form=UserCreationForm()
        return render(request, "autenticacion/registro.html", {"form":form})

    def post(self, request):
        """Send the user information to database."""
        form=UserCreationForm(request.POST)
        if form.is_valid():
            usuario=form.save()
            login(request, usuario)
            return redirect('Home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            
            return render(request, "autenticacion/registro.html", {"form":form})

def cerrar_sesion(request):
    """Close the user session."""
    logout(request)
    return redirect('Home')

def iniciar_sesion(request):
    """Log in the user session."""
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('Home')
            else:
                messages.error(request, "Usuario no válido.")
        else:
            messages.error(request, "Información incorrecta.")

    form=AuthenticationForm()
    return render(request, "autenticacion/login.html", {"form":form})
