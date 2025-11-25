from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo electrónico")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        labels = {
            "username": "Nombre de usuario",
            "password1": "Contraseña",
            "password2": "Confirmar contraseña",
        }
        help_texts = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})
        # Ayudas en español y con texto claro
        self.fields["username"].help_text = "Solo letras, numeros y @/./+/-/_"
        self.fields["password1"].help_text = (
            "Debe tener al menos 8 caracteres, no puede ser demasiado similar a tus datos, "
            "ni estar en listas comunes, ni ser solo numeros."
        )
        self.fields["password2"].help_text = "Repeti la contrasena para verificar."
