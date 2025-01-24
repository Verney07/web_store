from django.contrib import messages
#from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from carro.carro import Carro
from .models import Pedido, LineaPedido
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail


# Create your views here.
@login_required(login_url="/autenticacion/inicio_sesion")
def procesar_pedido(request):
    """Confirm the customer's order."""
    pedido=Pedido.objects.create(user=request.user)
    carro=Carro(request)
    lineas_pedido=list()

    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(
            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido
        ))
    
    LineaPedido.objects.bulk_create(lineas_pedido)

    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreusuario=request.user.username,
        email_usuario=request.user.email
        )

    messages.success(request, "El pedido se ha creado correctamente")
    return redirect('../tienda')
    #return redirect('listado_productos')
    #return render(request, "tienda/tienda.html", {"productos":productos})

def enviar_mail(**kwargs):
    """Seding e-mail to user when pushes 'Realizar pedido' button"""
    asunto="Gracias por realizar el pedido"

    mensaje=render_to_string("emails/pedido.html",{

        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nombreusuario": kwargs.get("nombreusuario"),
        "email_usuario": kwargs.get("email_usuario")
    })

    mensaje_texto=strip_tags(mensaje)

    from_email="pruebas2.django2024@gmail.com"
    to=kwargs.get("email_usuario")
    #to="ve.soto.le@gmail.com"

    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)
