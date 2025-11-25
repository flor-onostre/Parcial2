from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render

from .forms import ContactoForm


def contacto_view(request):
    form = ContactoForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        email = EmailMessage(
            subject=f"Contacto de {data['nombre']}",
            body=data["mensaje"],
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[data["email"]],
        )
        email.send(fail_silently=False)
        messages.success(request, "Mensaje enviado.")
        return redirect("/contacto/")
    return render(request, "contacto/form.html", {"form": form})

# Create your views here.
