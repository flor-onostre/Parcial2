import json
import requests
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render

from .forms import ContactoForm


def _enviar_brevo(destino: str, asunto: str, cuerpo: str, reply_to: str | None = None):
    """Envía correo usando la API v3 de Brevo."""
    if not settings.BREVO_API_KEY or not settings.BREVO_SENDER_EMAIL:
        raise ValueError("Brevo no está configurado (falta API KEY o sender).")
    payload = {
        "sender": {
            "email": settings.BREVO_SENDER_EMAIL,
            "name": settings.BREVO_SENDER_NAME or settings.BREVO_SENDER_EMAIL,
        },
        "to": [{"email": destino}],
        "subject": asunto,
        "htmlContent": f"<p>{cuerpo}</p>",
    }
    if reply_to:
        payload["replyTo"] = {"email": reply_to}
    resp = requests.post(
        "https://api.brevo.com/v3/smtp/email",
        headers={
            "api-key": settings.BREVO_API_KEY,
            "Content-Type": "application/json",
            "accept": "application/json",
        },
        data=json.dumps(payload),
        timeout=10,
    )
    resp.raise_for_status()
    return resp.json()


def contacto_view(request):
    form = ContactoForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        destino = data.get("email")
        asunto = f"Contacto de {data['nombre']}"
        cuerpo = data["mensaje"]
        try:
            if settings.BREVO_API_KEY:
                _enviar_brevo(destino, asunto, cuerpo, reply_to=destino)
            else:
                # Fallback SMTP/local: lo deja igual que antes por compatibilidad local
                email = EmailMessage(
                    subject=asunto,
                    body=cuerpo,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[destino] if destino else [settings.EMAIL_HOST_USER],
                    bcc=[settings.EMAIL_HOST_USER] if settings.EMAIL_HOST_USER else None,
                    reply_to=[destino] if destino else None,
                )
                email.send(fail_silently=False)
            messages.success(request, "Mensaje enviado.")
        except Exception as exc:
            messages.error(request, f"No se pudo enviar el correo: {exc}")
        return redirect("/contacto/")
    return render(request, "contacto/form.html", {"form": form})

# Create your views here.
