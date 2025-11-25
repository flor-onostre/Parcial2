from django.urls import path
from . import views

urlpatterns = [
    path("productos/", views.productos_view, name="productos"),
    path("productos/nuevo/", views.producto_crear, name="producto_crear"),
    path("carrito/", views.carrito_view, name="carrito"),
    path("carrito/agregar/<int:pk>/", views.agregar_carrito, name="carrito_agregar"),
    path("carrito/quitar/<int:pk>/", views.quitar_carrito, name="carrito_quitar"),
]
