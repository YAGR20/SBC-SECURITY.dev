from django.db import models

class EventoSeguridad(models.Model):
    fecha = models.DateTimeField()
    ip = models.GenericIPAddressField()
    tipo_ataque = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.tipo_ataque} - {self.ip} - {self.fecha}"
