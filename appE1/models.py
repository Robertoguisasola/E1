from django.db import models
from datetime import datetime


# Create your models here.
class Articulo(models.Model):
    titular = models.CharField(max_length=100, default='')
    entradilla = models.TextField()
    cuerpo = models.TextField()
    fecha = models.DateTimeField(default=datetime.now, blank=True)

    @property
    def __str__(self):
        return self.titular
