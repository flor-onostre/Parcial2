from django.shortcuts import redirect, render

from .forms import FotoForm
from .models import Foto


def galeria_view(request):
    fotos = Foto.objects.order_by("-creada")
    return render(request, "galeria/lista.html", {"fotos": fotos})


def subir_foto(request):
    form = FotoForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("/galeria/")
    return render(request, "galeria/form.html", {"form": form})

# Create your views here.
