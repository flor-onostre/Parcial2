from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import TareaCBV


class TareaListView(ListView):
    model = TareaCBV
    template_name = "tareas_cbv/lista.html"
    context_object_name = "tareas"
    ordering = ["-fecha_creacion"]


class TareaCreateView(CreateView):
    model = TareaCBV
    fields = ["titulo", "descripcion"]
    template_name = "tareas_cbv/form.html"
    success_url = reverse_lazy("tareas_cbv_lista")


class TareaUpdateView(UpdateView):
    model = TareaCBV
    fields = ["titulo", "descripcion"]
    template_name = "tareas_cbv/form.html"
    success_url = reverse_lazy("tareas_cbv_lista")


class TareaDeleteView(DeleteView):
    model = TareaCBV
    template_name = "tareas_cbv/confirmar_borrar.html"
    success_url = reverse_lazy("tareas_cbv_lista")


class TareaDetailView(DetailView):
    model = TareaCBV
    template_name = "tareas_cbv/detalle.html"
    context_object_name = "tarea"

# Create your views here.
