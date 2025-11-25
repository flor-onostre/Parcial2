import io

from django.http import FileResponse
from django.shortcuts import get_object_or_404, redirect, render
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from .forms import ReporteForm
from .models import Reporte


def lista_reportes(request):
    reportes = Reporte.objects.order_by("-fecha")
    form = ReporteForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("/reportes/")
    return render(request, "informes/lista.html", {"reportes": reportes, "form": form})


def reporte_pdf(request, pk):
    reporte = get_object_or_404(Reporte, pk=pk)
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, 750, reporte.nombre)
    p.setFont("Helvetica", 12)
    text = p.beginText(80, 700)
    for line in reporte.contenido.splitlines():
        text.textLine(line)
    p.drawText(text)
    p.drawString(80, 650, f"Fecha: {reporte.fecha}")
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f"{reporte.nombre}.pdf")

# Create your views here.
