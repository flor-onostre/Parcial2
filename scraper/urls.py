from django.urls import path
from . import views

urlpatterns = [
    path("scraper/", views.buscar, name="scraper"),
]
