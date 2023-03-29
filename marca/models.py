from django.db import models

from core.models import Audit, WithoutDeleteManager


class Marca(Audit):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    objects = WithoutDeleteManager()

    def __str__(self):
        return self.nombre
