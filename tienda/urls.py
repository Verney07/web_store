"""Views tienda's app."""
from django.urls import path
from .import views

urlpatterns = [
    path('', views.tienda, name="Tienda"),
]
