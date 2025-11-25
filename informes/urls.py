from django.urls import path
from . import views

urlpatterns = [
    path("reportes/", views.lista_reportes, name="reportes_lista"),
    path("reporte/<int:pk>/pdf/", views.reporte_pdf, name="reporte_pdf"),
]
