from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import RegistroForm


def registro_view(request):
    form = RegistroForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user, backend=settings.AUTHENTICATION_BACKENDS[0])
        messages.success(request, "Usuario creado y logueado.")
        return redirect("/panel/")
    return render(request, "cuentas/registro.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("/panel/")
    error = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Bienvenido.")
            return redirect("/panel/")
        error = "Usuario o contraseña incorrecta"
    return render(request, "cuentas/login.html", {"error": error})


def logout_view(request):
    logout(request)
    messages.info(request, "Sesión cerrada.")
    return redirect("/")


@login_required
def panel_view(request):
    return render(request, "cuentas/panel.html")

# Create your views here.
