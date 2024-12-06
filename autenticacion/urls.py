"""URLs to configure app 'contacto'"""
from django.urls import path

from .import views

urlpatterns = [
    path('', views.autenticacion, name="Autenticacion"),
]
