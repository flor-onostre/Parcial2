from django.db import models


class Foto(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to="fotos/")
    creada = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.titulo

# Create your models here.
