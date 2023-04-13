from django.db import models
from conductoresApp.models import Conductor


# Create your models here.
class Vehiculo(models.Model):
    # id = models.IntegerField(primary_key=True, max_length=6)
    modelo = models.CharField('Modelo', max_length=4,null=False)
    placa = models.CharField('Placa',max_length=7, unique=False, null=False)
    capacidad = models.CharField('Capacidad',max_length=7, unique=False)
    conductor_id = models.ForeignKey(Conductor, related_name='conductor_id', on_delete=models.CASCADE, null=True, blank=True, default="")

class Meta:

    verbose_name = 'Vehiculo'
    verbose_name_prural = 'Vehiculos'

    def __str__(self):
        return self.placa