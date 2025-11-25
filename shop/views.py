from decimal import Decimal

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductoForm
from .models import Producto


def _init_carrito(session):
    if "carrito" not in session:
        session["carrito"] = {}


def productos_view(request):
    productos = Producto.objects.all()
    return render(request, "shop/productos.html", {"productos": productos})


@staff_member_required
def producto_crear(request):
    form = ProductoForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("/productos/")
    return render(request, "shop/producto_form.html", {"form": form})


def carrito_view(request):
    _init_carrito(request.session)
    items = []
    for pid, item in request.session["carrito"].items():
        subtotal = Decimal(str(item["precio"])) * item["cantidad"]
        items.append({**item, "id": pid, "subtotal": subtotal})
    total = sum(i["subtotal"] for i in items)
    return render(request, "shop/carrito.html", {"items": items, "total": total})


def agregar_carrito(request, pk):
    _init_carrito(request.session)
    producto = get_object_or_404(Producto, pk=pk)
    carrito = request.session["carrito"]
    item = carrito.get(str(producto.id), {"nombre": producto.nombre, "precio": float(producto.precio), "cantidad": 0})
    item["cantidad"] += 1
    carrito[str(producto.id)] = item
    request.session.modified = True
    return redirect("/carrito/")


def quitar_carrito(request, pk):
    _init_carrito(request.session)
    carrito = request.session["carrito"]
    if str(pk) in carrito:
        del carrito[str(pk)]
        request.session.modified = True
    return redirect("/carrito/")

# Create your views here.
