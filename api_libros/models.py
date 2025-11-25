from django.db import models


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    anio = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.titulo

# Create your models here.
