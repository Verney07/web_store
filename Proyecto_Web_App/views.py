from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return render(request, "Proyecto_Web_App/home.html")


def servicios(request):

    return render(request, "Proyecto_Web_App/servicios.html")


def tienda(request):

    return render(request, "Proyecto_Web_App/tienda.html")


def blog(request):

    return render(request, "Proyecto_Web_App/blog.html")


def contacto(request):

    return render(request, "Proyecto_Web_App/contacto.html")
