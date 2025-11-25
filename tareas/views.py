from django.shortcuts import get_object_or_404, redirect, render

from .forms import TareaForm
from .models import Tarea


def lista_tareas(request):
    tareas = Tarea.objects.order_by("-fecha_creacion")
    return render(request, "tareas/lista.html", {"tareas": tareas})


def crear_tarea(request):
    form = TareaForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("/tareas/")
    return render(request, "tareas/form.html", {"form": form, "accion": "Crear"})


def editar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    form = TareaForm(request.POST or None, instance=tarea)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("/tareas/")
    return render(
        request, "tareas/form.html", {"form": form, "accion": "Editar", "tarea": tarea}
    )


def borrar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == "POST":
        tarea.delete()
        return redirect("/tareas/")
    return render(request, "tareas/confirmar_borrar.html", {"tarea": tarea})

# Create your views here.
