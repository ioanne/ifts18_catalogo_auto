from django.db import models

from core.models import Audit, WithoutDeleteManager


class Categoria(Audit):

    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    objects = WithoutDeleteManager()

    def __str__(self):
        return self.nombre


# # Ejemplo de como usar el ORM de django
# categorias = Categoria.objects.all()
# # <QuerySet [<Categoria: Categoria object (1)>, <Categoria: Categoria object (2)>]>
# categorias = categorias.filter(nombre="Sedan")
# categorias = categorias.exclude(nombre="Sedan")
# categoria = categorias.last()
# categoria # va a ser el objeto Categoria, no vas a poder hacer mas consultas SQL.
