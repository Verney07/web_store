"""A 'view.py' that allow send us e-mails."""
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import FormularioContacto

# Create your views here.

def contacto(request):
    """A view that render 'contacto' web page."""
    if request.method=="POST":
        formulario_contacto=FormularioContacto(request.POST)
        if formulario_contacto.is_valid():
            
            data_form=formulario_contacto.cleaned_data

            subject=data_form['nombre']
            message=data_form['contenido']+ " "+ data_form['email']
            email_from=settings.EMAIL_HOST_USER
            recipient_list=['pruebas.django2024@gmail.com']

            try:
                send_mail(subject, message, email_from, recipient_list)
                
                return redirect("/contacto/?valido")
            
            except:
                return redirect("/contacto/?novalido")

    else:
        formulario_contacto=FormularioContacto() #Creates an empty form
            
    return render(request, "contacto/contacto.html", {'miFormulario': formulario_contacto})
