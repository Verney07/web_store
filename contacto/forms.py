from django import forms


class FormularioContacto(forms.Form):
    """A form for the 'contacto' menu option."""
    nombre=forms.CharField(label="Nombre", required=True)

    email=forms.CharField(label="E-mail", required=True)
    
    contenido=forms.CharField(label="Contenido")