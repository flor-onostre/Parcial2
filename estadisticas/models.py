from django.db import models


class Visita(models.Model):
    pagina = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.pagina} - {self.fecha}"

# Create your models here.
