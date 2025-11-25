from django.db import models


class Reporte(models.Model):
    nombre = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.nombre

# Create your models here.
