from django.db import models

class EquipoFutbol(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    fundacion = models.PositiveIntegerField()
    estadio = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre
