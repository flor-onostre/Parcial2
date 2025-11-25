from django.urls import path
from . import views

urlpatterns = [
    path("estadisticas/", views.dashboard, name="dashboard"),
]
