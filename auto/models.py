from django.db import models

from core.models import Audit, WithoutDeleteManager


class WithoutAudi(WithoutDeleteManager):
    def get_queryset(self):
        return super().get_queryset().exclude(marca__nombre="Audi")


class Auto(Audit):
    marca = models.ForeignKey("marca.Marca", on_delete=models.DO_NOTHING)
    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    año = models.IntegerField()
    precio = models.IntegerField()

    # Si quieren filtrar el modelo para todos los objetos, se debe hacer desde un manager
    objects = WithoutAudi()
    objects_all = models.Manager()
    
    def get_rojos(self):
        # A todo lo anterior le suma el filtro de color rojo
        return self.objects.filter(color="rojo")
        


    
# auto = Auto()
# auto.objects = models.Manager() # inyectando la dependencia models.Manager()
# auto.objects.all()
