from django.urls import path
from . import views

urlpatterns = [
    path("galeria/", views.galeria_view, name="galeria_lista"),
    path("galeria/subir/", views.subir_foto, name="galeria_subir"),
]
