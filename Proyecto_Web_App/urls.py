"""URL's 'Proyecto Web App'"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Proyecto_Web_App import views

urlpatterns = [
    path('', views.home, name="Home"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)