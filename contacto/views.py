from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render

from .forms import ContactoForm


def contacto_view(request):
    form = ContactoForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        to_list = [data["email"]] if data.get("email") else []
        bcc_list = [settings.EMAIL_HOST_USER] if settings.EMAIL_HOST_USER else []
        try:
            email = EmailMessage(
                subject=f"Contacto de {data['nombre']}",
                body=data["mensaje"],
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=to_list or bcc_list,  # si el usuario no puso email válido, al menos se envía al admin
                bcc=bcc_list,
                reply_to=[data["email"]] if data.get("email") else None,
            )
            email.send(fail_silently=False)
            messages.success(request, "Mensaje enviado.")
        except Exception as exc:
            messages.error(request, f"No se pudo enviar el correo: {exc}")
        return redirect("/contacto/")
    return render(request, "contacto/form.html", {"form": form})

# Create your views here.
