from django.db.models import Count
from django.db.models.functions import TruncDate
from django.shortcuts import render

from .models import Visita


def dashboard(request):
    visitas_por_dia = (
        Visita.objects.annotate(dia=TruncDate("fecha"))
        .values("dia")
        .annotate(total=Count("id"))
        .order_by("dia")
    )
    mas_visitadas = (
        Visita.objects.values("pagina")
        .annotate(total=Count("id"))
        .order_by("-total")[:5]
    )
    contexto = {
        "labels_dias": [v["dia"].strftime("%Y-%m-%d") for v in visitas_por_dia],
        "data_dias": [v["total"] for v in visitas_por_dia],
        "labels_paginas": [v["pagina"] for v in mas_visitadas],
        "data_paginas": [v["total"] for v in mas_visitadas],
    }
    return render(request, "estadisticas/dashboard.html", contexto)

# Create your views here.
